# Generated by Django 2.2.7 on 2019-11-25 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen_name', models.CharField(max_length=20)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('capacity', models.IntegerField(default=6)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.CharField(choices=[('M', '오전(6시~12시)'), ('A', '오후(12시~18시)'), ('N', '밤/심야(18시~24시)')], max_length=1)),
                ('kitchen_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Kitchen_info')),
            ],
        ),
    ]
