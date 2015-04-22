# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.contenttypes.admin import GenericTabularInline
from backend.models import *
from django.utils.translation import ugettext_lazy as _


class MyAdminSite(AdminSite):
    site_header = site_title = _(u'爱在人间')


admin_site = MyAdminSite(name='love')


@admin.register(Option, site=admin_site)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'zh_content', 'en_content', 'score', 'add_time')
    exclude = ('add_time',)
    search_fields = ('zh_content', 'en_content')
    list_display_links = ('id', 'zh_content',)


@admin.register(QuestionClass, site=admin_site)
class QuestionClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'zh_content', 'en_content', 'add_time')
    exclude = ('add_time',)
    search_fields = ('zh_content', 'en_content')
    list_display_links = ('id', 'zh_content',)


@admin.register(Question, site=admin_site)
class QuestionAdmin(admin.ModelAdmin):
    # fields = ('zh_content', 'en_content', 'en_content', 'options')
    list_display = ('id', 'zh_content', 'en_content', 'question_class', 'add_time')
    exclude = ('add_time',)
    search_fields = ('zh_content', 'en_content', 'id')
    list_display_links = ('id', 'zh_content',)
    list_filter = ('question_class',)


@admin.register(ResultExplain, site=admin_site)
class ResultExplainAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_score', 'max_score', 'add_time')
    exclude = ('add_time',)

    list_display_links = ('id', 'min_score',)


@admin.register(Questions, site=admin_site)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'zh_title', 'en_title', 'is_need_pay', 'price','detail_price', 'add_time')
    exclude = ('add_time',)

    list_display_links = ('id', 'zh_title',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        question_classes = QuestionClass.objects.all()
        extra_context['question_classes_set'] = question_classes
        return super(QuestionsAdmin, self).change_view(request, object_id,
                                                       form_url, extra_context=extra_context)


    def add_view(self, request,  form_url='', extra_context=None):
        extra_context = extra_context or {}
        question_classes = QuestionClass.objects.all()
        extra_context['question_classes_set'] = question_classes
        return super(QuestionsAdmin, self).add_view(request,
                                                       form_url, extra_context=extra_context)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "question":
            us = request.META['PATH_INFO'].split('/')
            qsid = request.POST.getlist('question')
            if unicode.isdigit(us[-2]):
                if not qsid:
                    qid = us[-2]
                    qs = Questions.objects.get(id=qid)
                    kwargs["queryset"] = qs.question.all()
                else:
                    qs = Question.objects.filter(id__in=qsid)
                    kwargs["queryset"] = qs
            elif us[-2] == 'add':
                if not qsid:
                    kwargs["queryset"] = Question.objects.none()
                else:
                    qs = Question.objects.filter(id__in=qsid)
                    kwargs["queryset"] = qs
            else:
                kwargs["queryset"] = Question.objects.none()
        if db_field.name == "explain":
            us = request.META['PATH_INFO'].split('/')
            if unicode.isdigit(us[-2]):
                qid = us[-2]
                qs = Questions.objects.get(id=qid)
                kwargs["queryset"] = qs.explain.all()
            elif us[-2] == 'add':
                qsid = request.POST.getlist('explain')
                if not qsid:
                    kwargs["queryset"] = Question.objects.none()
                else:
                    qs = ResultExplain.objects.filter(id__in=qsid)
                    kwargs["queryset"] = qs
            else:
                kwargs["queryset"] = ResultExplain.objects.none()
        return super(QuestionsAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(UserAnwser, site=admin_site)
class UserAnwserAdmin(admin.ModelAdmin):
    readonly_fields = list_display = ('id', 'user', 'questions', 'question', 'option','user_result', 'add_time')
    # exclude = ('add_time',)
    list_display_links = ('id', 'user',)
    list_filter = ('question__question_class',)


@admin.register(EvalUser, site=admin_site)
class EvalUserAdmin(admin.ModelAdmin):
    readonly_fields = list_display = ('id', 'name','get_mytest', 'sex', 'age', 'email', 'phone', 'add_time')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'email', 'phone')
    ordering = ('-id',)
    list_filter = ('sex', 'add_time')

@admin.register(UserResult, site=admin_site)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'questions', 'is_pay','get_anwser_url','get_scores','get_explain_url', 'price', 'our_trade_no', 'pay_time','is_pay_detail','detail_price', 'detail_our_trade_no', 'detail_pay_time', 'add_time')
    exclude = ('add_time',)
    fields = ('user', 'questions', 'score_explain', 'is_pay', 'price', 'our_trade_no', 'pay_time','is_pay_detail','detail_price', 'detail_our_trade_no', 'detail_pay_time', 'add_time')
    readonly_fields = ('user', 'questions', 'is_pay', 'price', 'our_trade_no', 'pay_time', 'score_explain','is_pay_detail','detail_price', 'detail_our_trade_no', 'detail_pay_time', 'add_time')
    list_display_links = ('id', 'user',)
    # search_fields = ('user__id',)


@admin.register(UserScoreExplain, site=admin_site)
class UserScoreExplainAdmin(admin.ModelAdmin):
    readonly_fields = list_display = ('id', 'user_result', 'score', 'explain', 'add_time')
    list_display_links = ('id', 'user_result',)
    # exclude = ('add_time',)
    # fields = ('user_result', 'score', 'explain')

