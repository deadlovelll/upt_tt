from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'named_url', 'parent', 'menu_name']
    prepopulated_fields = {'named_url': ('title',)}

admin.site.register(MenuItem, MenuItemAdmin)
