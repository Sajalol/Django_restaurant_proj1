from .models import Reservation
from django import forms


class ReservationForm(forms.ModelForm):
    model = Reservation
    fields = ('table', 'party', 'spot',)