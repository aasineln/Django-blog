from django.db import models


class Advertisement(models.Model):
    ADV_HEADINGS_CHOICES = [
        ('WO', 'Work'),
        ('SP', 'Sport'),
        ('CA', 'Cars'),
    ]
    ADV_STATUS_CHOICES = [
        ('ACT', 'Active'),
        ('NOACT', 'Not Active'),
        ('ARCH', 'Archive'),
    ]
    ADV_AUTHOR_CHOICES = [
        ('UN', 'Unknown'),
    ]
    ADV_TYPES_CHOICES = [
        ('BU', 'Buy'),
        ('SE', 'Sell'),
        ('RE', 'Rent'),
    ]

    title = models.CharField(max_length=1500, db_index=True, verbose_name='заголовок')
    description = models.TextField(max_length=3000, default='default text', verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publicated_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    publicated_end_at = models.DateTimeField(auto_now=True, verbose_name='дата окончания публикации')
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    type = models.CharField(max_length=100, null=True, choices=ADV_TYPES_CHOICES)
    author = models.CharField(max_length=100, null=True, choices=ADV_AUTHOR_CHOICES)
    heading = models.CharField(max_length=100,  null=True, choices=ADV_HEADINGS_CHOICES)

    @property
    def price_to_dollar(self):
        return int(self.price / 70)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

