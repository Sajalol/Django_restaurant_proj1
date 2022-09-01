from django.db import models
import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
# from django.contrib.auth.models import User



class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120, default='Kings Place')
    city = models.CharField(max_length=120, default='Kristiansund')
    country = models.CharField(max_length=120, default='Norway')

class Table(models.Model):
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return str(self.seats)


class Reservation(models.Model):

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'
        unique_together = ('date', 'time', 'seats')

    TIME_LIST = (
        (0, '10:00 – 11:00'),
        (1, '11:00 – 12:00'),
        (2, '12:00 – 13:00'),
        (3, '13:00 – 14:00'),
        (4, '14:00 – 15:00'),
        (5, '15:00 – 16:00'),
        (6, '16:00 – 17:00'),
        (7, '17:00 – 18:00'),
        (8, '18:00 – 19:00'),
        (9, '19:00 – 20:00'),
        (10,'20:00 – 21:00'),
        (11,'21:00 – 22:00'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    phone = PhoneNumberField()
    number_of_guests = models.IntegerField(default=3,)
    date = models.DateField(default=datetime.date.today)
    time = models.IntegerField(choices=TIME_LIST, default=0)
    approved = models.BooleanField(default=True)
    seats = models.ForeignKey(Table, on_delete=models.CASCADE, default='',)

    def __str__(self) -> str:
        return self.user.username

class Menu(models.Model):
    nameOfFood = models.CharField(max_length=30)
    meat = models.CharField(max_length=30)
    allergy = models.CharField(max_length=30)
    details = models.CharField(max_length=999, default="")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=149)
    image = CloudinaryField('image', default='/static/img/chicken_tandori_default.jpg')
