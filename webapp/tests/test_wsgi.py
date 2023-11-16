# test_wsgi.py
import pytest
from django.core.wsgi import get_wsgi_application

@pytest.mark.django_db
def test_wsgi_default_settings():
    # Test that the WSGI application uses the correct settings module
    assert 'webapp.settings' in get_wsgi_application().__module__, "WSGI application must be configured with 'webapp.settings'"