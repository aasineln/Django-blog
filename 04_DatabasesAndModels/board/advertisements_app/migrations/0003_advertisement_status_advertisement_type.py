# Generated by Django 4.1.2 on 2022-11-07 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0002_remove_advertisement_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisement_status', to='advertisements_app.advertisementstatus'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisement_type', to='advertisements_app.advertisementtype'),
        ),
    ]
