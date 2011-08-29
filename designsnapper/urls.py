from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

import designsnapper.views as views


urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'marketing/index.html'}),
    (r'manage', views.ManageView.as_view()),
    (r'page', views.PageView.as_view()),
    (r'debug', views.DebugView.as_view())
)
