from django.conf.urls.defaults import *
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.simple import direct_to_template

import designsnapper.views as views

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('designsnapper.urls')),
    (r'^manage/$', views.ManageView.as_view()),
    (r'^page/$', views.PageView.as_view()),
    (r'^debug/$', views.DebugView.as_view()),

    (r'^accounts/create/$', 'designsnapper.views.create_new_user'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'authentication_form': AuthenticationForm,
        'template_name': 'login.html',}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/designsnapper/',}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
