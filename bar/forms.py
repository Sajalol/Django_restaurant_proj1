from django import forms
from django.forms import fields
from .models import Reservation

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'number_of_guests', 'date', 'time',)