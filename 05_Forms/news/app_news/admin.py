from django.contrib import admin
from .models import News, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'is_active']
    list_filter = ['is_active']
    inlines = [CommentInLine]
    actions = ['mark_active', 'mark_inactive']

    def mark_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_inactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_active.short_description = 'Перевести в статус active'
    mark_inactive.short_description = 'Перевести в статус inactive'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['news', 'name', 'short_comment', 'created', 'updated']
    list_filter = ['name']
    actions = ['deleted_by_admin']

    def deleted_by_admin(self, request, queryset):
        queryset.update(text='Удалено администратором')

    deleted_by_admin.short_description = 'Очистить текст и подписать Удалено админстратором'
