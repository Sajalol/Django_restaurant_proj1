from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Restaurant(models.Model):
    name = models.CharField(max_length=120)

class Customer(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Table(models.Model):
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

class Reservation(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    party = models.ForeignKey('Customer', on_delete=models.CASCADE)
    spot = models.DateField()

class Menu(models.Model):
    nameOfFood = models.CharField(max_length=30)
    meat = models.CharField(max_length=30)
    allergy = models.CharField(max_length=30)
    food_details = models.CharField(max_length=150)