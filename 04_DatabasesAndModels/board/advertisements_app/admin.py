from django.contrib import admin

# Register your models here.
from advertisements_app.models import Advertisement, AdvStatus, AdvAuthor, AdvHeading, \
    AdvType


@admin.register(Advertisement, AdvType, AdvAuthor, AdvHeading, AdvStatus)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
