from django import forms
from django.forms import fields
from .models import Reservation, Table
from django.core import validators
from django.forms import CharField
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

# Reservation form

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('phone', 'number_of_guests', 'date', 'time', 'seats',)
        widgets = {
            'date':DateInput(),
        }
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date