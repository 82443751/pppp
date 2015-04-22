# -*- coding: UTF-8 -*-
from datetime import datetime
import json
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.response import TemplateResponse, SimpleTemplateResponse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __
from django.views.decorators.csrf import csrf_exempt
from Eval import settings
from alipay.alipay import create_direct_pay_by_user, notify_verify
from backend.models import *
from django.utils import translation
from django.core.urlresolvers import reverse
from payment.views import logger1


def eval_index(request, eid=-1):
    """
    开始测试前的页面，需要填写个人信息
    :param request:
    :param eid:
    :return:
    """
    eval_name = None
    eval_age = None
    eval_sex = None
    eval_email = None
    eval_phone = None
    err_info = None
    if request.method == 'POST':
        eval_name = request.POST.get('eval_name', '')
        eval_age = request.POST.get('eval_age', '')
        eval_sex = request.POST.get('eval_sex', '')
        eval_email = request.POST.get('eval_email', '')
        eval_phone = request.POST.get('eval_phone', '')
        if eval_name != '' and eval_age != '' and eval_sex != '' and eval_email != '' and eval_phone != '':
            try:
                users = EvalUser.objects.filter(name=eval_name, sex=eval_sex, email=eval_email, phone=eval_phone)
                if users:
                    user=users[0]
                else:
                    user = EvalUser(name=eval_name, age=eval_age, sex=eval_sex, email=eval_email, phone=eval_phone)
                    user.save()
                request.session['user_id'] = user.id
                return redirect(reverse('eval_test', kwargs={'eid': eid}))
            except Exception, e:
                err_info = e.message
        else:
            err_info = _(u'请完整填写以下信息')
    return render_to_response('backend/eval.html', {
        'err_info': err_info,
        "title": _(u"测试题"),
        "content": _(u"请先填写以下个人信息，然后点击下一步开始测试"),
        "eid": eid,
        "lang_set": True,
        "eval_name": eval_name,
        "eval_age": eval_age,
        "eval_sex": eval_sex,
        "eval_email": eval_email,
        "eval_phone": eval_phone,
        "view_name": "eval_index",
        "lang_code": request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'zh'),
    },context_instance=RequestContext(request))
    # return render_to_response('backend/eval.html',
    # {
    # 'err_info': err_info,
    #                               "title": _(u"测试题"),
    #                               "content": _(u"请先填写以下个人信息，然后点击下一步开始测试"),
    #                               "eid": eid,
    #                               "eval_name": eval_name,
    #                               "eval_age": eval_age,
    #                               "eval_sex": eval_sex,
    #                               "eval_email": eval_email,
    #                               "eval_phone": eval_phone,
    #                               },
    #                           )


def eval_test(request, eid=-1):
    """
    显示测试题进行测试
    :param request:
    :param eid:
    :return:
    """
    user_id = request.session.get('user_id', -1)
    if user_id == -1:
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr

    btn_text = _(u"提交")
    can_test = True
    if eid == -1:
        eval_obj = {
            "title": _(u"爱在人间测试"),
            "content": _(u"请从主站相关测试题进入本测试")
        }
    else:
        language = translation.get_language()
        try:
            questions = Questions.objects.get(id=eid)
            eval_obj = {
                "title": questions.get_title(language),
                "content": questions.get_content(language),
                "questions": questions.question,
            }
            can_test = True
        except Questions.DoesNotExist:
            eval_obj = {
                "title": _(u"爱在人间测试"),
                "content": _(u"未找到你要进行的测试")
            }
    return render_to_response('backend/eval_test.html',
                              {"button_text": btn_text,
                               "title": _(u"测试题"),
                               "can_test": can_test,
                               "lang_set": False,
                               "eid": eid,
                               "view_name": "eval_result",
                               "lang_code": language,
                               "eval": eval_obj},
                              context_instance=RequestContext(request))

def gen_order_no():
    import time
    import random
    on ='%s%s' % ( time.strftime('%Y%m%d%H%M%S'),random.randint(100,999))
    return on
def eval_result(request,eid=-1):
    """
    显示测试题的结果
    :param request:
    :return:
    """
    user_id = request.session.get('user_id', -1)
    # eid = request.POST.get('eid', -1)
    if user_id == -1 or eid == -1 or request.method == "GET":
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr

    btn_text = _(u"支付")
    language = translation.get_language()
    logger1.debug("language:"+language)
    try:
        user = EvalUser.objects.get(id=user_id)
        questions = Questions.objects.get(id=eid)
        eval_obj = {
            "title": questions.get_title(language),
            "content": questions.get_content(language),
            "questions": questions.question,
            }
        class_score = {}
        qs = questions.question.all()
        user_anwsers = []
        for q in qs:
            option_id = request.POST.get('option_' +str(q.id))
            if option_id is None:
                if user_anwsers:
                    UserAnwser.objects.filter(id__in=user_anwsers).delete()
                return render_to_response('backend/eval_test_error.html',
                              {"button_text": _(u"返回"),
                               "title": _(u"测试题"),
                               "info": _(u"请全部填写完成后再点击'提交'按钮。"),
                               })
            option = Option.objects.get(id=option_id)
            score = option.score
            if q.question_class is None:
                if -1 in class_score:
                    class_score[-1] = class_score[-1] + score
                else:
                    class_score[-1] = score
            else:
                if q.question_class.id in class_score:
                    class_score[q.question_class.id] = class_score[q.question_class.id] + score
                else:
                    class_score[q.question_class.id] = score

            ua = UserAnwser.objects.create(user=user, questions=questions, question = q, option = option)
            user_anwsers.append(ua.id)
            # ua.save()

        user_result= UserResult.objects.create(user=user, questions=questions)
        if user_anwsers:
            UserAnwser.objects.filter(id__in=user_anwsers).update(user_result=user_result)
        # if created:
        user_result.price = questions.price
        user_result.our_trade_no = gen_order_no()
        user_result.detail_price = questions.detail_price
        user_result.detail_our_trade_no = gen_order_no()
        user_result.save()
        ret_explain={}
        for explain in questions.explain.all():
            if explain.question_class is None and -1 in class_score:
                # explain.user_score=class_score[-1]
                if explain.max_score >= class_score[-1] >= explain.min_score:
                    use,created=UserScoreExplain.objects.get_or_create(user_result=user_result,explain=explain)
                    if created:
                        use.score=class_score[-1]
                        use.save()
                    if explain.get_simple_content(language) and explain.get_content(language):
                        ret_explain[-1]=use
            elif explain.question_class is not None:
                if explain.question_class.id in class_score:
                    if explain.max_score >= class_score[explain.question_class.id] >= explain.min_score:
                        use,created=UserScoreExplain.objects.get_or_create(user_result=user_result,explain=explain)
                        if created:
                            use.score=class_score[explain.question_class.id]
                            use.save()
                        if explain.get_simple_content(language) and explain.get_content(language):
                            ret_explain[explain.question_class.id] = use
        if user_result.price == 0:
            pay_url = create_direct_pay_by_user(user_result.detail_our_trade_no, __(u'爱在人间测试报告'),
                                            questions.get_title(language), user_result.detail_price, language)
        else:
            pay_url = create_direct_pay_by_user(user_result.our_trade_no, __(u'爱在人间测试报告'),
                                            questions.get_title(language), user_result.price, language)
    except Questions.DoesNotExist, e:
        eval_obj = {
            "title": _(u"爱在人间测试"),
            "content": _(u"未找到你要进行的测试")
        }
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr
    return render_to_response('backend/eval_result.html',
                              {"button_text": btn_text,
                               "title": _(u"测试题"),
                               "user_result": user_result,
                               "ret_explain":ret_explain,
                               "is_need_pay": questions.is_need_pay,
                               "lang_set": False,
                               "eid": eid,
                               "pay_url": pay_url,
                               "price": questions.price,
                               "lang_code": language,
                               "view_name": "eval_result",
                               "eval": eval_obj})



def eval_full_result(request,eid=-1):
    """
    显示测试题的完整结果
    :param request:
    :return:
    """
    user_id = request.session.get('user_id', -1)
    # eid = request.POST.get('eid', -1)
    if user_id == -1 or eid == -1:
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr
    pay_url = ""
    btn_text = _(u"支付")
    language = translation.get_language()
    try:
        user = EvalUser.objects.get(id=user_id)
        questions = Questions.objects.get(id=eid)
        eval_obj = {
            "title": questions.get_title(language),
            "content": questions.get_content(language),
            "questions": questions.question,
            }

        user_result= UserResult.objects.get(user=user, questions=questions)
        explains =UserScoreExplain.objects.filter(user_result=user_result)
        # if not user_result.is_pay:
        #     pay_url = create_direct_pay_by_user(user_result.our_trade_no,__( u'爱在人间测试报告'),
        #                                     questions.get_title(language), user_result.price, language)

        if not user_result.is_pay_detail:
            pay_url = create_direct_pay_by_user(user_result.detail_our_trade_no, __(u'爱在人间测试报告'),
                                            questions.get_title(language), user_result.detail_price, language)
    except Questions.DoesNotExist, e:
        eval_obj = {
            "title": _(u"爱在人间测试报告"),
            "content": _(u"未找到你要进行的测试")
        }
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr
    return render_to_response('backend/eval_result.html',
                              {"button_text": btn_text,
                               "title": _(u"测试题"),
                               "user_result": user_result,
                               "explains":explains,
                               "is_need_pay": not user_result.is_pay_detail,
                               "pay_url": pay_url,
                               "lang_set": False,
                               "eid": eid,
                               "price": questions.price,
                               "lang_code": language,
                               "view_name": "eval_result",
                               "eval": eval_obj})


def eval_detail_result(request,eid=-1):
    """
    显示测试题的更详细结果
    :param request:
    :return:
    """
    user_id = request.session.get('user_id', -1)
    # eid = request.POST.get('eid', -1)
    if user_id == -1 or eid == -1:
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr
    pay_url = ""
    btn_text = _(u"支付")
    language = translation.get_language()
    try:
        user = EvalUser.objects.get(id=user_id)
        questions = Questions.objects.get(id=eid)
        eval_obj = {
            "title": questions.get_title(language),
            "content": questions.get_content(language),
            "questions": questions.question,
            }

        user_result= UserResult.objects.get(user=user, questions=questions)
        explains =UserScoreExplain.objects.filter(user_result=user_result)
        if not user_result.is_pay_detail:
            pay_url = create_direct_pay_by_user(user_result.detail_our_trade_no, __(u'爱在人间测试报告'),
                                            questions.get_title(language), user_result.detail_price, language)
    except Questions.DoesNotExist, e:
        eval_obj = {
            "title": _(u"爱在人间测试报告"),
            "content": _(u"未找到你要进行的测试")
        }
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr
    return render_to_response('backend/eval_result.html',
                              {"button_text": btn_text,
                               "title": _(u"测试题"),
                               "user_result": user_result,
                               "explains":explains,
                               "is_need_pay": not user_result.is_pay_detail,
                               "pay_url": pay_url,
                               "lang_set": False,
                               "is_detail": True,
                               "eid": eid,
                               "price": questions.detail_price,
                               "lang_code": language,
                               "view_name": "eval_result",
                               "eval": eval_obj})



@login_required
def eval_result_for_admin(request,user_id=-1,eid=-1, result_id=-1):
    """
    显示测试题的所有结果
    :param request:
    :return:
    """
    # eid = request.POST.get('eid', -1)
    if user_id == -1 or eid == -1 or result_id==-1:
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr
    pay_url = ""
    btn_text = _(u"支付")
    language = translation.get_language()
    try:
        user = EvalUser.objects.get(id=user_id)
        questions = Questions.objects.get(id=eid)
        eval_obj = {
            "title": questions.get_title(language),
            "content": questions.get_content(language),
            "questions": questions.question,
            }

        user_result= UserResult.objects.get(id=result_id)
        explains =UserScoreExplain.objects.filter(user_result=user_result)

        pay_url = ""
    except Questions.DoesNotExist, e:
        eval_obj = {
            "title": _(u"爱在人间测试报告"),
            "content": _(u"未找到你要进行的测试")
        }
        hrr = HttpResponseRedirect(reverse('eval_index', kwargs={'eid': eid}))
        return hrr
    return render_to_response('backend/eval_result.html',
                              {"button_text": btn_text,
                               "title": _(u"测试题"),
                               "user_result": user_result,
                               "explains":explains,
                               "is_need_pay": False,
                               "pay_url": pay_url,
                               "lang_set": False,
                               "eid": eid,
                               "price": questions.price,
                               "lang_code": language,
                               "view_name": "eval_result",
                               "eval": eval_obj})


def set_site_language(request, language="zh", eid=1, view_name='eval_index'):
    """设置语言
    """
    if view_name == '':
        view_name = 'eval_index'
    translation.activate(language)
    settings.CURRENT_LANG_CODE = language
    hrr = HttpResponseRedirect(reverse(view_name, kwargs={'eid': eid}))
    hrr.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return hrr



@csrf_exempt
def alipay_notify(request):
    """
    Handler for notify_url for asynchronous updating billing information.
    Logging the information.
    """
    logger1.info('>>notify url handler start...')
    if request.method == 'POST':
        if notify_verify(request.POST):
            logger1.info('pass verification...')
            tn = request.POST.get('out_trade_no')
            trade_no = request.POST.get('trade_no')
            logger1.info('Change the status of bill %s' % tn)
            is_detail = False
            urs=UserResult.objects.filter(our_trade_no=tn)
            if urs.exists():
                bill = UserResult.objects.get(our_trade_no=tn)
            else:
                urs=UserResult.objects.filter(detail_our_trade_no=tn)
                if urs.exists():
                    is_detail = True
                else:
                    return HttpResponse("fail")

            trade_status = request.POST.get('trade_status')
            language = request.POST.get('extra_common_param','zh')
            if is_detail:
                logger1.info('the status of bill %s changed to %s' % (tn, trade_status))
                if not bill.is_pay_detail:
                    bill.is_pay_detail = True
                    bill.detail_pay_time = datetime.now()
                    bill.detail_trade_no = trade_no
                    bill.save()
                if bill.is_pay_detail:
                    to_email = bill.user.email
                    if to_email:
                        explains =UserScoreExplain.objects.filter(user_result=bill)# bill.score_explain.all()
                        content = []
                        for explain in explains:
                            content.append(explain.explain.get_detail(language))
                        send_report_mail(to_email, title=bill.questions.get_title(language), content='<br>'.join(content))

            else:
                logger1.info('the status of bill %s changed to %s' % (tn, trade_status))
                if not bill.is_pay:
                    bill.is_pay = True
                    bill.pay_time = datetime.now()
                    bill.trade_no = trade_no
                    bill.save()
                if bill.is_pay:
                    to_email = bill.user.email
                    if to_email:
                        explains =UserScoreExplain.objects.filter(user_result=bill)# bill.score_explain.all()
                        content = []
                        for explain in explains:
                            content.append(explain.explain.get_content(language))
                        send_report_mail(to_email, title=bill.questions.get_title(language), content='<br>'.join(content))
            logger1.info('##info: Status of %s' % trade_status)
            logger1.info('return success')
            return HttpResponse("success")
    logger1.info('return fail')
    return HttpResponse("fail")


def alipay_return(request):
    """
    Handler for synchronous updating billing information.
    """
    logger1.info('>> return url handler start')
    if notify_verify(request.GET):
        tn = request.GET.get('out_trade_no')
        trade_no = request.GET.get('trade_no')
        logger1.info('Change the status of bill %s' % tn)
        bill = UserResult.objects.get(our_trade_no=tn)
        trade_status = request.GET.get('trade_status')
        logger1.info('the status changed to %s' % trade_status)

        is_detail = False
        urs=UserResult.objects.filter(our_trade_no=tn)
        if urs.exists():
            bill = UserResult.objects.get(our_trade_no=tn)
        else:
            urs=UserResult.objects.filter(detail_our_trade_no=tn)
            if urs.exists():
                is_detail = True
            else:
                return HttpResponse("fail")

        trade_status = request.POST.get('trade_status')
        language = request.POST.get('extra_common_param','zh')
        if is_detail:
            if not bill.is_pay_detail:
                    bill.is_pay_detail = True
                    bill.detail_pay_time = datetime.now()
                    bill.detail_trade_no = trade_no
                    bill.save()
        else:
            if not bill.is_pay:
                bill.is_pay = True
                bill.pay_time = datetime.now()
                bill.trade_no = trade_no
                bill.save()
        eval_obj = {
            "title": bill.questions.get_title(language),
            "content": bill.questions.get_content(language),
            "questions": bill.questions.question,
            }
        explains =UserScoreExplain.objects.filter(user_result=bill)# bill.score_explain.all()
        user_result=bill

        if is_detail and  not user_result.is_pay_detail:
            pay_url = create_direct_pay_by_user(user_result.detail_our_trade_no, __(u'爱在人间详细测试报告'),
                                            bill.questions.get_title(language), user_result.detail_price, language)
        return render_to_response('backend/eval_result.html',
                              {
                               "title": _(u"测试题"),
                               "user_result": bill,
                               "is_need_pay": not is_detail and  not user_result.is_pay_detail,
                               "lang_set": False,
                               "is_detail": is_detail,
                               "explains": explains,
                               "eid": bill.questions.id,
                               "pay_url": pay_url,
                               "lang_code": language,
                               "view_name": "alipay_return",
                               "eval": eval_obj})
    return HttpResponseRedirect(reverse('payment_error'))


def payment_error(request):
    """
    支付错误显示
    :param request:
    :return:
    """
    btn_text = _(u"提交")
    can_test = False
    eval_obj = {
        "title": _(u"爱在人间测试"),
        "content": _(u"支付错误，请从主站相关测试题进入本测试")
    }
    return render_to_response('backend/eval_test.html',

                              {"button_text": btn_text,
                               "title": _(u"测试题"),
                               "can_test": can_test,
                               "eid": "0",
                               "lang_set": False,
                               "lang_code": request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'zh'),
                               "view_name": "payment_error",
                               "eval": eval_obj},
                              context_instance=RequestContext(request))


def send_report_mail(to_mail=None, title=None, content=None):
    '''
    发送电子邮件
    :param to_mail:
    :param title:
    :param content:
    :return:
    '''
    try:
        logger1.info('send mail to %s:' % to_mail)
        subject, from_email, to = _(u'爱在人间测试报告'), 'kevinma@zhongkeyun.com', to_mail
        text_content = content
        html_content = '<h2>%s</h2><p>%s</p>' % (title, text_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        logger1.info('send mail to %s success' % to_mail)
    except Exception,e:
        logger1.error('send mail to %s fail:%s' % (to_mail,e.message))


def eval_question_autocomplete(request):
    '''
    提供添加问题时方便复用
    :param request:
    :return:
    '''
    key=request.GET.get('term','').strip()
    ret_qs=[]
    response=HttpResponse(content_type='text/json')
    if key!='':
        language = translation.get_language()
        qs=Question.objects.filter(Q(zh_content__contains=key) or Q(en_content__contains=key))[:10]
        if qs:
            for q in qs:
                ret_qs.append({'value':q.id,'label':q.get_content(language)})
    response.write(json.dumps(ret_qs))
    return response


def eval_get_questions_by_class(request):
    '''
    获取某一类别的问题
    :param request:
    :return:
    '''
    key=request.GET.get('qs_id','').strip()
    exist_qs_id=request.GET.get('exist_qs_id',None)
    if exist_qs_id:
        exist_qs_id=exist_qs_id.split(',')
    else:
        exist_qs_id=[]
    ret_qs=[]
    response=HttpResponse(content_type='text/json')
    if key!='':
        try:
            qclass=QuestionClass.objects.get(id=key)
            # language = translation.get_language()
            qs=Question.objects.filter(question_class=qclass).exclude(id__in=exist_qs_id)#.values_list('id','zh_content','en_content')

            language = translation.get_language()
            if qs:
                for q in qs:
                    ret_qs.append((q.id,q.get_content(language)))
            # ret_qs=list(qs)
        except:
            pass
    response.write(json.dumps(ret_qs))
    return response


def more_help(request):
    """
    获取更多帮助
    :param request:
    :return:
    """
    can_test = False
    eval_obj = {
        "title": _(u"爱在人间测试"),
        "content": _(u"如果您想获得专业咨询师的协谈，请与爱在人间咨询与培训教育机构联系，联系方式为:")
    }
    return render_to_response('backend/more_help.html',

                              {
                               "lang_set": False,
                               "lang_code": request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'zh')},
                              context_instance=RequestContext(request))

