# Generated by Django 2.2.6 on 2019-11-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen_info',
            name='image',
            field=models.CharField(max_length=20),
        ),
    ]
