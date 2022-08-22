from django.db import models
import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120, default='Kings Place')
    city = models.CharField(max_length=120, default='Kristiansund')
    country = models.CharField(max_length=120, default='Norway')

class Customer(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.email

class Table(models.Model):
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return str(self.seats)


class Reservation(models.Model):
    name = models.CharField(max_length=50, default="",)
    email = models.EmailField(default="",)
    phone = models.IntegerField(default=12345678,)
    number_of_guests = models.IntegerField(default=3,)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default='00:00',)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'

    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    nameOfFood = models.CharField(max_length=30)
    meat = models.CharField(max_length=30)
    allergy = models.CharField(max_length=30)
    details = models.CharField(max_length=160, default="")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=149)
    image = CloudinaryField('image', default='/static/img/chicken_tandori_default.jpg')
