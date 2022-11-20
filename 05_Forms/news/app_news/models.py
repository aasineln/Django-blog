from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=400, default='', verbose_name='Заголовок')
    description = models.CharField(max_length=5000, verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news')

    class Meta:
        ordering = ['-created_at']


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


