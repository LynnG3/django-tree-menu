"""Template tags for rendering tree menus."""
import time

from typing import Dict, Set, List, Optional
from django import template

from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name: str) -> dict:
    """
    Renders a tree menu with the specified name.

    Args:
        context: Template context containing the request
        menu_name: Name of the menu to render

    Returns:
        dict: Dict containing menu items tree and active item
    """
    start_time = time.time()
    request = context['request']
    current_url = request.path

    menu_items = MenuItem.objects.filter(
        menu_name=menu_name
    ).select_related('parent').order_by('position')

    items_dict = {item.id: item for item in menu_items}

    active_item = next(
        (item for item in menu_items if item.get_url() == current_url),
        None
    )

    expanded_items = set()
    if active_item:
        current = active_item
        while current:
            expanded_items.add(current.id)
            current = items_dict.get(current.parent_id)

    tree = [
        {
            'item': item,
            'children': get_children(
                items_dict,
                item.id,
                expanded_items,
                active_item
            ),
            'is_expanded': item.id in expanded_items,
            'is_active': item == active_item
        }
        for item in menu_items if not item.parent
    ]

    end_time = time.time()
    print(f"Menu rendering took: {end_time - start_time:.4f} seconds")
    return {
        'menu_items': tree,
        'active_item': active_item
    }


def get_children(
    items_dict: Dict[int, MenuItem],
    parent_id: int,
    expanded_items: Set[int],
    active_item: Optional[MenuItem]
) -> List[dict]:
    """
    Recursively builds a tree of child menu items.

    Args:
        items_dict: Dictionary of all menu items indexed by ID
        parent_id: ID of the parent item
        expanded_items: Set of IDs of items that should be expanded
        active_item: Currently active menu item

    Returns:
        List of dictionaries representing child menu items
    """
    return [
        {
            'item': item,
            'children': get_children(
                items_dict,
                item.id,
                expanded_items,
                active_item
            ),
            'is_expanded': item.id in expanded_items,
            'is_active': item == active_item
        }
        for item in items_dict.values()
        if item.parent_id == parent_id
    ]
