from django import template
from django.urls import resolve
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu_name=menu_name)

    current_url = resolve('/').url_name
    active_item = menu_items.filter(named_url=current_url).first()

    def build_menu(items, parent=None):
        menu = []
        for item in items:
            if item.parent == parent:
                children = build_menu(items, item)
                menu.append({
                    'item': item,
                    'children': children,
                    'active': active_item == item or active_item in children
                })
        return menu

    menu_structure = build_menu(menu_items)
    return menu_structure
