# Generated by Django 3.2.15 on 2022-08-24 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0029_alter_reservation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bar.customer'),
        ),
    ]
