# Generated by Django 3.2.14 on 2022-07-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0003_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, default=149, max_digits=5),
        ),
    ]