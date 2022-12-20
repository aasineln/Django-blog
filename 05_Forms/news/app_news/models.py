import os
from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse
from app_users.models import User


def path_and_filename(instance, filename):
    now = datetime.datetime.now()
    added_time_name = str(now.strftime("%d%m%y-%H-%M-%S")) + '_'
    new_file_name = added_time_name + filename
    return os.path.join('', new_file_name)


class News(models.Model):
    title = models.CharField(max_length=400, default='', verbose_name='Заголовок')
    description = models.CharField(max_length=5000, verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name='URL')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # avatar = models.ImageField(upload_to=path_and_filename, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']
        permissions = [
            ('can_publish', 'Может публиковать'),
        ]


class ImageModel(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=path_and_filename, null=True, blank=True)

    def __str__(self):
        return str(self.photo)


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


# class Author(models.Model):
#     user = models.CharField(max_length=100)
#     news = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True)
#
#     def __str__(self):
#         return self.user
#
#     @staticmethod
#     def published_news(self):
#         return len(News.objects.filter(author=self.user))
