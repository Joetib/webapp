# test for webapp/wsgi.py
import pytest
from django.core.wsgi import get_wsgi_application

@pytest.fixture
def wsgi_application():
    return get_wsgi_application()

def test_wsgi_application(wsgi_application):
    assert wsgi_application is not None