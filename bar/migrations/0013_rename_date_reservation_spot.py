# Generated by Django 3.2.15 on 2022-08-18 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0012_reservation_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='date',
            new_name='spot',
        ),
    ]