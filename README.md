# 🌳 Django Tree Menu
Django application for creating and managing hierarchical menus
with efficient database queries and template tag rendering.

All requirements implemented according to specification:

1. ✅ **Template Tag Based**: Menu rendering through custom template tag `{% draw_menu 'menu_name' %}`
2. ✅ **Smart Expansion**: 
   - Auto-expands all items above active item
   - Shows first level of nested items under active item
3. ✅ **Database Driven**: Menu structure stored in database
4. ✅ **Admin Integration**: Django admin interface support
5. ✅ **URL-based Activation**: Active item determined by current page URL
6. ✅ **Multiple Menus**: Support for multiple menus identified by name
7. ✅ **Flexible URLs**: Supports both direct URLs and named URLs
8. ✅ **Query Efficient**: Single database query per menu render using `select_related`


## 🚀 Quick Start

1. Clone the repository:
```bash
git@github.com:LynnG3/django-tree-menu.git
cd django-tree-menu
```

2. Create and activate virtual environment:
```bash
# For Unix/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create superuser to access admin panel:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

7. Access the admin panel at `http://127.0.0.1:8000/admin/` and create menu items

8. Use in your templates:
```html
{% load menu_tags %}
{% draw_menu 'main_menu' %}
```

## 💡 Implementation Details

- **Template Tag**: Implemented in `templatetags/menu_tags.py`
- **Database Model**: Single `MenuItem` model with self-reference for hierarchy
- **Query Optimization**: Uses `select_related()` for efficient data retrieval
- **URL Handling**: Supports both named URLs (`'app:name'`) and direct paths (`'/path/'`)

## 🛠 Technical Requirements

- Python 3.11+
- Django 5.2
- No additional dependencies required

## 📝 License

MIT License