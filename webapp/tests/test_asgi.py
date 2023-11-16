# test_asgi.py
import pytest
from django.core.asgi import get_asgi_application

@pytest.mark.django_db
def test_asgi_application():
    assert get_asgi_application() is not None, "ASGI application should be instantiated"