# test_asgi.py
import pytest
from django.test import SimpleTestCase
from django.core.asgi import get_asgi_application

@pytest.mark.django_db
class TestASGI(SimpleTestCase):

    def test_get_asgi_application(self):
        # Ensure that the ASGI application can be loaded
        try:
            get_asgi_application()
            loaded = True
        except Exception as e:
            loaded = False
        self.assertTrue(loaded, "ASGI application should be loadable")