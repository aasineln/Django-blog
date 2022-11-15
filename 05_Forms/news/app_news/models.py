from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=400, default='', verbose_name='Заголовок')
    description = models.CharField(max_length=5000, verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news')

    class Meta:
        ordering = ['-created_at']
