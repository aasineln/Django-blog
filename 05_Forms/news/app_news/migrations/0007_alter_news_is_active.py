# Generated by Django 4.1.2 on 2022-11-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_news_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]