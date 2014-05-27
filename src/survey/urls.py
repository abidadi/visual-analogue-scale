from django.conf.urls import patterns, url

from survey import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<survey_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<survey_id>\d+)/results/$', views.results, name='results'),
)  