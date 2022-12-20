from django.db import models
import os
import datetime


def path_and_filename(instance, filename):
    now = datetime.datetime.now()
    added_time_name = str(now.strftime("%d%m%y-%H-%M-%S")) + '_'
    new_file_name = added_time_name + filename
    return os.path.join('files/', new_file_name)


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование товара')
    code = models.CharField(max_length=30, verbose_name='Артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class File(models.Model):
    file = models.FileField(upload_to=path_and_filename)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
