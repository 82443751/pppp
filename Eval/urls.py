from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
import backend
from backend.admin import admin_site
from backend import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Eval.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin_site.urls)),
    #   url(r'^eval/(?P<eid>\d+)/$', views.eval_index, name="eval_index"),
    url(r'^set_site_language/(?P<language>\w+)/(?P<eid>\d+)/(?P<view_name>[A-z_]*)/$', views.set_site_language, name="set_site_language"),
    # (r'^i18n/', include('django.conf.urls.i18n')),
    # url(r'^$', views.eval_list),
    url(r'^alipay_return/', views.alipay_return, name="alipay_return"),
    url(r'^alipay_notify/', views.alipay_notify, name="alipay_notify"),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^eval_get_questions_by_class/', views.eval_get_questions_by_class, name="eval_get_questions_by_class"),
    url(r'^$', include(admin_site.urls)),

)
urlpatterns += i18n_patterns('',
                             url(r'^eval_index/(?P<eid>\d+)/$', views.eval_index, name="eval_index"),
                             url(r'^eval_test/(?P<eid>\d+)/$', views.eval_test, name="eval_test"),
                             url(r'^eval_result/(?P<eid>\d+)/$', views.eval_result, name="eval_result"),
                             url(r'^eval_result_for_admin/(?P<user_id>\d+)/(?P<eid>\d+)/(?P<result_id>\d+)/$', views.eval_result_for_admin, name="eval_result_for_admin"),
                             url(r'^eval_full_result/(?P<eid>\d+)/$', views.eval_full_result, name="eval_full_result"),
                             url(r'^payment_error/$', views.payment_error, name="payment_error"),
                             url(r'^eval_question_autocomplete/$', views.eval_question_autocomplete, name="eval_question_autocomplete"),
)