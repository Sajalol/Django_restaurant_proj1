from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views import generic, View
from .models import Restaurant, Menu, Reservation, Table, User
from django.shortcuts import redirect
from django.contrib import messages
from django.forms import Form
from django.contrib.auth.decorators import login_required
from .forms import ReserveTableForm
from django.views.generic.edit import DeleteView

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
                messages.error(request, 'Invalid form submission, correct the lines with error.')

    context = {'form': reserve_form}

    return render(request, 'reservation.html', context)




# List reservations

def list_view(request):
    context = {}

    context["dataset"] = Reservation.objects.all()

    return render(request, "list_view.html", context)



# detail view

def detail_view(request, reservation_id):


    context ={}

    reservation = get_object_or_404(Reservation, id=reservation_id)
    context["data"] = Reservation.objects.get(id = reservation_id)
    return render(request, "detail_view.html", context)


# delete view
def delete_view(request, reservation_id):

    context ={}

    reservation = get_object_or_404(Reservation, id=reservation_id)
    context["data"] = Reservation.objects.get(id = reservation_id)
    reservation.delete()
    return render(request, "delete_view.html", context)
