from django.contrib import admin
from . import models
from django.contrib.auth.models import User, Group

# title of the admin page
admin.site.site_header = 'Expenditure Management System'


# display table form the item table in the admin panel
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ('category',)
    search_fields = ('name', 'category')
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'quantity')
        }),
    )

# Register your models here.
admin.site.register(models.Item, ItemAdmin)


# unregister the Group model from admin.
admin.site.unregister(Group)
