# test_apps.py
from django.apps import apps
from pages.apps import PagesConfig

def test_pages_config():
    assert PagesConfig.name == 'pages'
    assert apps.get_app_config('pages').name == 'pages'