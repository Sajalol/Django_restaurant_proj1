# Generated by Django 3.2.15 on 2022-09-01 20:24

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfFood', models.CharField(max_length=30)),
                ('meat', models.CharField(max_length=30)),
                ('allergy', models.CharField(max_length=30)),
                ('details', models.CharField(default='', max_length=999)),
                ('price', models.DecimalField(decimal_places=2, default=149, max_digits=5)),
                ('image', cloudinary.models.CloudinaryField(default='/static/img/chicken_tandori_default.jpg', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(default='Kings Place', max_length=120)),
                ('city', models.CharField(default='Kristiansund', max_length=120)),
                ('country', models.CharField(default='Norway', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('min_people', models.IntegerField()),
                ('max_people', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('number_of_guests', models.IntegerField(default=3)),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.IntegerField(choices=[(0, '10:00 – 11:00'), (1, '11:00 – 12:00'), (2, '12:00 – 13:00'), (3, '13:00 – 14:00'), (4, '14:00 – 15:00'), (5, '15:00 – 16:00'), (6, '16:00 – 17:00'), (7, '17:00 – 18:00'), (8, '18:00 – 19:00'), (9, '19:00 – 20:00'), (10, '20:00 – 21:00'), (11, '21:00 – 22:00')], default=0)),
                ('approved', models.BooleanField(default=True)),
                ('seats', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='bar.table')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'reservation',
                'verbose_name_plural': 'reservations',
                'unique_together': {('date', 'time', 'seats')},
            },
        ),
    ]
