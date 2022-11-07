from django.contrib import admin

# Register your models here.
from advertisements_app.models import Advertisement, AdvertisementType, AdvertisementAuthor, AdvertisementHeading, \
    AdvertisementStatus


@admin.register(Advertisement, AdvertisementType, AdvertisementAuthor, AdvertisementHeading, AdvertisementStatus)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
