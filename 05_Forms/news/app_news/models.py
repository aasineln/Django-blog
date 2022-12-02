from django.db import models
from django.db.models import ManyToManyField
from django.urls import reverse
from taggit.models import RuTaggedItem

from app_users.models import User
from taggit.managers import TaggableManager


class News(models.Model):
    title = models.CharField(max_length=400, default='', verbose_name='Заголовок')
    description = models.CharField(max_length=5000, verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name='URL')
    # tags = models.ManyToManyField('NewsTags', related_name='news_tags')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']
        permissions = [
            ('can_publish', 'Может публиковать'),
        ]


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, verbose_name='Имя')
    text = models.CharField(max_length=500, default='', verbose_name='текст комментария')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Comment by {}'.format(self.name)

    def short_comment(self):
        if len(self.text) < 15:
            return self.text
        return f'{self.text[:15]}...'


class NewsTags(models.Model):
    news = models.ManyToManyField(News)
    tag = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag
