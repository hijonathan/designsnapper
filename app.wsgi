import os, sys
sys.path.append('/var/www/chief/public_html')
os.environ['DJANGO_SETTINGS_MODULE'] = 'designsnapper.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()