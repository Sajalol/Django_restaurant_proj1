from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Restaurant, Menu, Reservation, Customer, Table, User
from django.shortcuts import redirect
from django.contrib import messages
from django.forms import Form
from django.contrib.auth.decorators import login_required
from .forms import ReserveTableForm

class RestaurantList(generic.ListView):
    model = Restaurant
    template_name = 'index.html'

class MenuList(generic.ListView):
    model = Menu
    template_name = 'menu.html'


# Reservation form, requires you to login first
@login_required()
def reserve_table(request):
    reserve_form = ReserveTableForm()
    user = None
    if request.user.is_authenticated:
        
    

        if request.method == 'POST':
            reserve_form = ReserveTableForm(request.POST)

            if reserve_form.is_valid():
                form = reserve_form.save(commit=False)
                form.user = request.user
                form.save()
                messages.success(request, 'Your reservation has been submitted successfully.')
            else:
                messages.error(request, 'Invalid form submission, correct the ones with error.')

    context = {'form': reserve_form}

    return render(request, 'reservation.html', context)
