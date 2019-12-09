# Generated by Django 2.2.7 on 2019-12-09 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_remove_kitchen_info_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen_info',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
