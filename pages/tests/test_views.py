# test_views.py
import pytest
from django.urls import reverse
from django.test import RequestFactory
from pages import views

@pytest.fixture
def request_factory():
    return RequestFactory()

def test_homepage_view(request_factory):
    request = request_factory.get('/')
    response = views.homepage(request)
    assert response.status_code == 200