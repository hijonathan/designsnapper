from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

import designsnapper.views as views


urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'marketing/index.html'}),
    (r'^platform/$', direct_to_template, {'template': 'marketing/platform.html'}),
    (r'^demo/$', direct_to_template, {'template': 'marketing/platform.html'}),
    (r'^pricing/$', direct_to_template, {'template': 'marketing/platform.html'})
)
