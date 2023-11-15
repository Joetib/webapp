# test_webapp_urls.py
import pytest
from django.urls import reverse, resolve
from django.contrib import admin

def test_admin_url():
    path = reverse('admin:index')
    assert resolve(path).func.__name__ == admin.site.index.__name__

@pytest.mark.django_db
def test_homepage_url():
    path = reverse('homepage')
    assert resolve(path).view_name == 'homepage'