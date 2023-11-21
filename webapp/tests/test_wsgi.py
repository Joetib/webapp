# test_wsgi.py
import os
from django.core.wsgi import get_wsgi_application

def test_wsgi_default_settings():
    assert os.environ['DJANGO_SETTINGS_MODULE'] == 'webapp.settings'
    application = get_wsgi_application()
    assert application is not None