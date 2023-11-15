# test_pages.py
import pytest
from django.urls import reverse
from django.test import Client

@pytest.fixture
def client():
    return Client()

def test_homepage_status_code(client):
    url = reverse('homepage')
    response = client.get(url)
    assert response.status_code == 200

def test_homepage_template_used(client):
    url = reverse('homepage')
    response = client.get(url)
    assert 'homepage.html' in [t.name for t in response.templates]