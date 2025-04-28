""" Admin panel for tree_menu application.
"""
from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Модель для отображения меню в админке.
    """
    list_display = [
        'name',
        'menu_name',
        'url',
        'parent',
        'position'
    ]
    list_filter = ['menu_name']
    search_fields = ['name', 'url']
    ordering = ['menu_name', 'position']
