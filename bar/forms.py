from django import forms
from django.forms import fields
from .models import Reservation, Table
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'number_of_guests', 'date', 'time', 'seats',)
        widgets = {
            'date':DateInput(),
            'time':TimeInput(),
        }