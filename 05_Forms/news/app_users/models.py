from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Телефонный номер должен быть следующего формата: '+999999999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Номер телефона')
    published_news_count = models.IntegerField(default=0, verbose_name='Количество опубликованных новостей')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = (
            ('can_verify', 'Может верифицировать'),
            ('can_publich', 'Может публиковать новости')
        )

    def __str__(self):
        return self.user.username


class Profile2(models.Model):
    """
    Класс создан для тестирования связанной модели,
    не для выполнения Практической работы
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions = (
            ('view_kpi', 'Может просматривать kpi'),
            ('view_alarms', 'Может просматривать alarms')
        )
#
#
# class Profile(models.Model):

#     city = models.CharField(max_length=36, blank=True, null=True)
#     is_verified = models.BooleanField(default=False)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
#                                  message="Телефонный номер должен быть следующего формата: '+999999999'")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Номер телефона')
#     published_news_count = models.IntegerField(default=0, verbose_name='Количество опубликованных новостей')
