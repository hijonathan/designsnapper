from django.conf.urls.defaults import *

urlpatterns = patterns('guestbook.views',
    (r'^$', 'home'),
    (r'^sign$', 'create_greeting')
)