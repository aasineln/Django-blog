from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin, GroupAdmin
from django.contrib.auth.models import Group

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified')
    actions = ['mark_is_verified', 'mark_is_not_verified']

    def mark_is_verified(self, request, queryset):
        queryset.update(is_verified=True)

    def mark_is_not_verified(self, request, queryset):
        queryset.update(is_verified=False)

    mark_is_verified.short_description = 'Перевести в статус verified'
    mark_is_not_verified.short_description = 'Перевести в статус not verified'


class UserInline(admin.TabularInline):
    model = User.groups.through


class UserAdminCustom(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username',)

    # inlines = ['GroupInline']

    # def get_object(self, request, object_id, from_field=None):
    #    user_group = self.group_object.user_set.all()
    #    return user_group


class GroupAdminCustom(GroupAdmin):
    inlines = [UserInline]


admin.site.unregister(User)
admin.site.register(User, UserAdminCustom)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdminCustom)
# @admin.register(UserExtended)
# class User(admin.ModelAdmin):
#     list_display = ['username', 'email', 'city', 'is_verified']
