"""Test URLs for checking the application.
"""
from django.urls import path
from .views import test_menu

urlpatterns = [
    path('test-menu/', test_menu, name='test_menu'),
    path('abc/', test_menu, name='abc'),
    path('abc-1/', test_menu, name='abc_1'),
    path('abc-12/', test_menu, name='abc_12'),
    path('klm/', test_menu, name='klm'),
    path('opr/', test_menu, name='opr'),
]
