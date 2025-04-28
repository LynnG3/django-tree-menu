"""
Django Tree Menu Application

This application provides a flexible and efficient way to create and manage
hierarchical menus in Django projects. It supports multiple menus per page,
URL-based active item detection, and efficient database queries.

Features:
- Template tag based menu rendering
- Database-driven menu structure
- Django admin integration
- Named URL support
- Single database query per menu render
- Automatic active item detection
- Multi-level menu support
"""


default_app_config = 'src.tree_menu.apps.TreeMenuConfig'
