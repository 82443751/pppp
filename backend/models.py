# -*- coding: UTF-8 -*-
# from datetime import datetime
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


# class AnswerTemplate(models.Model):
#     u"""    可供选择的答案模板 """
#     zh_option = models.CharField(u"中文答案", max_length=800, help_text=u"格式：标号，说明，分值；标号，说明，分值（示例：A,轻微,1;B,正常,2）")
#     en_option = models.CharField(u"English Answer", max_length=800,
#                                  help_text=u"Format：Label，Desc，Score；Label，Desc，Score（示例：A,Faster,1;B,Lower,2）")
#     add_time = models.DateTimeField(u"添加时间", auto_now_add=True)
from Eval import settings



class Option(models.Model):
    u"""问题的可选项"""
    zh_content = models.CharField(_(u"中文"), max_length=300, help_text=_(u"示例：轻微"))
    en_content = models.CharField(_(u"英文"), max_length=300, help_text=_(u"Example: Lower"))
    score = models.IntegerField(_(u"分值"), default=1, help_text=_(u"该选项的分值"))
    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True)

    def get_content(self, language=settings.CURRENT_LANG_CODE):
        if language.startswith(settings.ZH_LANG_CODE):
            return self.zh_content
        else:
            return self.en_content

    def __unicode__(self):
        return u"%s[%s]" % (self.zh_content, self.score)

    class Meta:
        ordering = ['add_time']
        verbose_name = verbose_name_plural = _(u"问题可选项")


class QuestionClass(models.Model):
    u"""问题的类别"""
    zh_content = models.CharField(_(u"中文"), max_length=300)
    en_content = models.CharField(_(u"英文"), max_length=300)
    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True)

    def get_content(self, language=settings.CURRENT_LANG_CODE):
        if language.startswith(settings.ZH_LANG_CODE):
            return self.zh_content
        else:
            return self.en_content

    def __unicode__(self):
        return self.zh_content+"-"+self.en_content

    class Meta:
        ordering = ['add_time']
        verbose_name = verbose_name_plural = _(u"问题类别")


class Question(models.Model):
    u"""单条问题"""
    zh_content = models.CharField(_(u"中文"), max_length=500, db_index=True)
    en_content = models.CharField(_(u"英文"), max_length=500, db_index=True)
    question_class = models.ForeignKey(QuestionClass, blank=True, null=True, db_index=True)
    options = models.ManyToManyField(Option)
    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True)

    def get_content(self, language=settings.CURRENT_LANG_CODE):
        if language.startswith(settings.ZH_LANG_CODE):
            return self.zh_content
        else:
            return self.en_content

    def __unicode__(self):
        return self.zh_content

    class Meta:
        ordering = ['add_time', 'question_class']
        verbose_name = verbose_name_plural = _(u"问题")


class ResultExplain(models.Model):
    u"""结果分数说明"""
    question_class = models.ForeignKey(QuestionClass,blank=True, null=True, db_index=True)
    min_score = models.IntegerField(_(u"分值区间低值"), help_text=_(u"包含"))
    max_score = models.IntegerField(_(u"分值区间高值"), help_text=_(u"包含"))
    # user_score = models.IntegerField(_(u"用户得分"), help_text=u"", blank=True, null=True, db_index=True)
    zh_simple_content = RichTextField(_(u"简要说明"),config_name='awesome_ckeditor', blank=True, null=True)
    en_simple_content = RichTextField(_(u"简要说明[英文]"),config_name='awesome_ckeditor', blank=True, null=True)
    zh_content = RichTextField(_(u"详细说明"),config_name='awesome_ckeditor', blank=True, null=True)
    en_content = RichTextField(_(u"详细说明[英文]"),config_name='awesome_ckeditor', blank=True, null=True)
    zh_detail = RichTextField(_(u"更详细说明"),config_name='awesome_ckeditor', blank=True, null=True)
    en_detail = RichTextField(_(u"更详细说明[英文]"),config_name='awesome_ckeditor', blank=True, null=True)
    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True)

    def get_simple_content(self, language=settings.CURRENT_LANG_CODE):
        if language.startswith(settings.ZH_LANG_CODE):
            return self.zh_simple_content
        else:
            return self.en_simple_content

    def get_content(self, language=settings.CURRENT_LANG_CODE):
        if language.startswith(settings.ZH_LANG_CODE):
            return self.zh_content
        else:
            return self.en_content

    def get_detail(self, language=settings.CURRENT_LANG_CODE):
        if language.startswith(settings.ZH_LANG_CODE):
            return self.zh_detail
        else:
            return self.en_detail

    def __unicode__(self):
        return u"%s-%s[%s]" % (self.min_score, self.max_score, self.question_class)

    class Meta:
        ordering = ['add_time', ]
        verbose_name = verbose_name_plural = _(u"分数说明")


class Questions(models.Model):
    u"""单套测试"""
    zh_title = models.CharField(_(u"标题"), max_length=300, db_index=True)
    en_title = models.CharField(_(u"标题[英文]"), max_length=300, db_index=True)
    zh_content = models.CharField(_(u"说明"), max_length=500, blank=True, null=True)
    en_content = models.CharField(_(u"说明[英文]"), max_length=500, blank=True, null=True)
    question = models.ManyToManyField(Question,verbose_name=_(u'问题'))
    explain = models.ManyToManyField(ResultExplain, verbose_name=_( u'分值说明'))
    is_need_pay = models.BooleanField(_(u"是否需要付费"), default=False, db_index=True)
    price = models.FloatField(_(u"价格"), default=0)
    detail_price = models.FloatField(_(u"详细报告价格"), default=0)
    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True)

    def get_title(self, language=settings.CURRENT_LANG_CODE):
        if language.startswith(settings.ZH_LANG_CODE):
            return self.zh_title
        else:
            return self.en_title

    def get_content(self, language=settings.CURRENT_LANG_CODE):
        if language.startswith(settings.ZH_LANG_CODE):
            return self.zh_content
        else:
            return self.en_content

    def __unicode__(self):
        return self.zh_title

    class Meta:
        ordering = ['add_time']
        verbose_name = verbose_name_plural = _(u"单套测试")


class EvalUser(models.Model):
    u"""测试用户信息"""
    SEX_CHOICES = (('1', _(u'男')),('0', _(u'女')))
    name = models.CharField(_(u'姓名'), max_length=50, db_index=True)
    sex = models.CharField(_(u'性别'), max_length=1, choices=SEX_CHOICES, db_index=True)
    age = models.CharField(_(u'年龄'), max_length=4)
    email = models.EmailField(_(u'邮箱'))
    phone = models.CharField(_(u'手机'), max_length=20)
    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True)

    def get_mytest(self):
        return u'<a href="/admin/backend/userresult/?user__id=%s" target="_self">%s</a>' % (self.id, _(u'做过的测试'))
    get_mytest.allow_tags=True
    get_mytest.short_description=  _(u'做过的测试')
    def __unicode__(self):
        return u"%s-%s[%s]" % (self.name, self.sex, self.phone)

    class Meta:
        ordering = ['add_time',]
        verbose_name = verbose_name_plural = _(u"用户信息")



class UserResult(models.Model):
    u"""某套题用户的选择"""
    user = models.ForeignKey(EvalUser, db_index=True)
    questions = models.ForeignKey(Questions, db_index=True)
    score_explain = models.ManyToManyField(ResultExplain, through="UserScoreExplain", through_fields=('user_result', 'explain'))
    is_pay = models.BooleanField(_(u"是否已支付"), default=False, db_index=True)
    is_pay_detail= models.BooleanField(_(u"是否已支付详细报告"), default=False, db_index=True)
    price = models.FloatField(_(u"价格"), default=0)
    detail_price = models.FloatField(_(u"价格"), default=0)
    our_trade_no = models.CharField(_(u"订单号"),max_length=50,blank=True,null=True, default='')
    trade_no = models.CharField(_(u"支付宝订单号"),max_length=100,blank=True,null=True, default='')
    pay_time = models.DateTimeField(_(u"支付时间"), auto_now_add=True,default=datetime.now)

    detail_our_trade_no = models.CharField(_(u"详细报告订单号"),max_length=50,blank=True,null=True, default='')
    detail_trade_no = models.CharField(_(u"详细报告支付宝订单号"),max_length=100,blank=True,null=True, default='')
    detail_pay_time = models.DateTimeField(_(u"详细报告支付时间"), auto_now_add=True,default=datetime.now)

    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True)

    def __unicode__(self):
        return u"%s-%s[%s][%s]" % (self.user, self.questions, self.is_pay, self.id)

    def get_anwser_url(self):
        return format_html(u'<a href="/admin/backend/useranwser/?user_result__id='+str(self.id)+'" target="_blank">'+(u'查看问题')+'</a>')

    get_anwser_url.allow_tags = True
    get_anwser_url.short_description = _(u'查看用户选择的问题')

    def get_explain_url(self):
        return format_html(u'<a href="/zh/eval_result_for_admin/'+str(self.user.id)+'/'+str(self.questions.id)+'/'+str(self.id)+'/" target="_blank">'+(u'查看分数说明')+'</a>')

    get_explain_url.allow_tags = True
    get_explain_url.short_description = _(u'查看分数说明')


    def get_scores(self):
        se =UserScoreExplain.objects.filter(user_result=self)# self.score_explain.all()
        ret=[]
        for ex in se:
            if ex.explain.question_class:
                ret.append(str(ex.explain.question_class)+':'+str(ex.score))
            else:
                ret.append(str(ex.score))
        return ','.join(ret)

    get_scores.short_description = _(u'得分')

    class Meta:
        ordering = ['add_time', 'user', 'is_pay']
        verbose_name = verbose_name_plural = _(u"用户得分")

class UserAnwser(models.Model):
    u"""某套题用户的选择"""
    user = models.ForeignKey(EvalUser, db_index=True)
    questions = models.ForeignKey(Questions, db_index=True)
    question = models.ForeignKey(Question, db_index=True)
    option = models.ForeignKey(Option, db_index=True)
    user_result= models.ForeignKey(UserResult, null=True,blank=True,db_index=True)
    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True)

    def __unicode__(self):
        return u"%s-%s[%s]" % (self.user, self.questions, self.question)

    class Meta:
        ordering = ['add_time', 'user', 'questions']
        verbose_name = verbose_name_plural = _(u"用户选择")


class UserScoreExplain(models.Model):
    '''
    用户的得分说明
    '''
    user_result= models.ForeignKey(UserResult)
    explain = models.ForeignKey(ResultExplain)
    score = models.IntegerField(verbose_name=_(u"分值"),default=-1,blank=True)
    add_time = models.DateTimeField(_(u"添加时间"), auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return u"%s-%s" % (self.user_result, self.score)

    class Meta:
        ordering = ['add_time',]
        verbose_name = verbose_name_plural = _(u"用户的得分说明")

