from django.contrib import admin
from .models import Item, File


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'price']


@admin.register(File)
class FileAdmib(admin.ModelAdmin):
    list_display = ['id', 'created_at', ]
