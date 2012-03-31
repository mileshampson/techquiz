import os
import sys

path = '/srv/techquiz'
if path not in sys.path:
    sys.path.append(path)
path = '/srv/techquiz/src'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangosite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
