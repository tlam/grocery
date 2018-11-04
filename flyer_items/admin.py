from django.contrib import admin

from flyer_items.models import FlyerItem


class FlyerItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'sale_text', 'disclaimer_text', 'store', 'created_at',)
    list_filter = ('store',)
    readonly_fields = ('created_at',)
    search_fields = ['name']

admin.site.register(FlyerItem, FlyerItemAdmin)
