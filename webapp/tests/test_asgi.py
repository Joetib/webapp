# test_asgi.py
import pytest
from django.conf import settings
from webapp.asgi import application

@pytest.mark.django_db
def test_asgi_application():
    assert application.__class__.__name__ == "ASGIHandler", "ASGI application must be an instance of ASGIHandler"
    assert settings.ASGI_APPLICATION == 'webapp.asgi.application', "ASGI_APPLICATION setting must point to the correct application."