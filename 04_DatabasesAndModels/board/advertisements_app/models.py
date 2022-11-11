from django.db import models


class Advertisement(models.Model):
    ADV_STATUS_CHOICES = [
        ('ACT', 'Active'),
        ('NOACT', 'Not Active'),
        ('ARCH', 'Archive'),
    ]
    ADV_TYPES_CHOICES = [
        ('BU', 'Buy'),
        ('SE', 'Sell'),
        ('RE', 'Rent'),
    ]
    ADV_HEADINGS_CHOICES = [
        ('WO', 'Work'),
        ('SP', 'Sport'),
        ('CA', 'Cars'),
    ]
    ADV_AUTHOR_CHOICES = [
        ('UN', 'Unknown'),
    ]

    title = models.CharField(max_length=1500, db_index=True, verbose_name='заголовок')
    description = models.TextField(max_length=3000, default='default text', verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publicated_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    publicated_end_at = models.DateTimeField(auto_now=True, verbose_name='дата окончания публикации')
    price = models.FloatField(verbose_name='цена', default=0.0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    type = models.ForeignKey('AdvType', default='Buy', null=True, on_delete=models.CASCADE,
                             related_name='adv_type', choices=ADV_TYPES_CHOICES)
    author = models.ForeignKey('AdvAuthor', default='Unknown', null=True, on_delete=models.CASCADE,
                               related_name='adv_author', choices=ADV_AUTHOR_CHOICES)
    heading = models.ForeignKey('AdvHeading', default='Work', null=True, on_delete=models.CASCADE,
                               related_name='adv_heading', choices=ADV_HEADINGS_CHOICES)

    @property
    def price_to_dollar(self):
        return self.price / 70

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class AdvStatus(models.Model):
    name = models.CharField(max_length=100,verbose_name='Тип объявления')

    def __str__(self):
        return self.name


class AdvType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип объявления')

    def __str__(self):
        return self.name


class AdvAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    email = models.EmailField(max_length=200, verbose_name='email')
    phone = models.CharField(max_length=30, verbose_name='телефон')

    def __str__(self):
        return self.name


class AdvHeading(models.Model):
    name = models.CharField(max_length=200, verbose_name='наименовение рубрики')

    def __str__(self):
        return self.name
