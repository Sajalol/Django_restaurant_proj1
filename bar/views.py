from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Restaurant, Menu, Reservation, Customer, Table
from .forms import ReservationForm

class RestaurantList(generic.ListView):
    model = Restaurant
    template_name = 'index.html'

class MenuList(generic.ListView):
    model = Menu
    template_name = 'menu.html'

class ReservationList(generic.ListView):
    model = Reservation
    template_name = 'reservation.html'

    def reservation(self, request):
        reservation_form = ReservationForm(data=request.POST)
        if request.method == "POST":
            Table = request.POST.get('Table')
            Costumer = request.POST.get('Customer')
            spot = request.POST.get('spot')

            return render(
                request,
                "reservation.html",
                {
                    "Table": table,
                    "Costumer": costumer,
                    "spot": spot,
                }
            )