# Generated by Django 3.2.15 on 2022-09-01 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0040_auto_20220831_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='name',
        ),
    ]