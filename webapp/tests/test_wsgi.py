# test_wsgi.py
import os
from django.test import TestCase
from django.core.wsgi import get_wsgi_application

class WSGITestCase(TestCase):

    def setUp(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')

    def test_wsgi_default_settings(self):
        application = get_wsgi_application()
        self.assertIsNotNone(application, "WSGI application should not be None")