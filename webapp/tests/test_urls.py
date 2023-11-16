# test_webapp_urls.py
import pytest
from django.urls import reverse, resolve

@pytest.mark.django_db
def test_admin_url():
    path = reverse('admin:index')
    assert resolve(path).view_name == 'admin:index'

@pytest.mark.django_db
def test_homepage_url():
    path = reverse('homepage')
    assert resolve(path).view_name == 'homepage'