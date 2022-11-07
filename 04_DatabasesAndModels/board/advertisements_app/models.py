from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True, verbose_name='заголовок')
    description = models.TextField(max_length=3000, default='default text', verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publicated_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    publicated_end_at = models.DateTimeField(auto_now=True, verbose_name='дата окончания публикации')
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name='advertisement_type')
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisement_author')
    heading = models.ForeignKey('AdvertisementHeading', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisement_heading')



    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип объявления')

    def __str__(self):
        return self.name


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    email = models.EmailField(max_length=200, verbose_name='email')
    phone = models.CharField(max_length=30, verbose_name='телефон')

    def __str__(self):
        return self.name


class AdvertisementHeading(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименовение рубрики')

    def __str__(self):
        return self.name
