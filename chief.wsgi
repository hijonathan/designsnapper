import os, sys
sys.path.append('/var/www/public_html/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chief.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()