from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
import designsnapper.views as views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view()),
    url(r'manage', views.ManageView.as_view()),
    url(r'page', views.PageView.as_view()),
    url(r'debug', views.DebugView.as_view())
)