# Generated by Django 4.1.2 on 2022-11-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='text2',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Имя'),
        ),
    ]