from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('designsnapper.views',
    (r'^$', 'home'),
    (r'settings', 'settings'),
    (r'pages', 'pages'),
    (r'page', 'page'),
    (r'debug', 'debug')
)