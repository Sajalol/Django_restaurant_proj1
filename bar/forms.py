from django import forms
from django.forms import fields
from .models import Reservation, Table

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

# Reservation form

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'number_of_guests', 'date', 'time', 'seats',)
        widgets = {
            'date':DateInput(),
        }