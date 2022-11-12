from django.contrib import admin

# Register your models here.
from advertisements_app.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
