from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('designsnapper.views',
    (r'^$', 'home', name='home'),
    (r'settings', 'settings', name='settings'),
    (r'pages', 'pages', name='pages'),
    (r'page', 'page', name='page'),
    (r'debug', 'debug', name='debug')
)