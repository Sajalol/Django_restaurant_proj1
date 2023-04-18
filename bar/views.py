from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views import generic, View
from .models import Restaurant, Menu, Reservation, Table, User
from django.shortcuts import redirect
from django.contrib import messages
from django.forms import Form
from django.contrib.auth.decorators import login_required
from .forms import ReserveTableForm
from django.views.generic.edit import DeleteView
from django.core.exceptions import PermissionDenied
from django.contrib import messages

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
                return HttpResponseRedirect('reservation')
            else:
                messages.error(request, 'Invalid form submission, correct the lines with error.')

    context = {'form': reserve_form}

    return render(request, 'reservation.html', context)




# List of Reservations, requires admin or staff to access it. Also access to delete reservations

def list_view(request):
    if not request.user.is_staff:
        raise PermissionDenied("403..You need to be staff to access this page")
    
    context = {}

    context["dataset"] = Reservation.objects.all()

    return render(request, "list_view.html", context)



# Detail View needed to get ID for deletion

def detail_view(request, reservation_id):

    context ={}

    reservation = get_object_or_404(Reservation, id=reservation_id)
    context["data"] = Reservation.objects.get(id = reservation_id)


# Delete View, needed to be able to delete in list_view

def delete_view(request, reservation_id):


    reservation = get_object_or_404(Reservation, pk=reservation_id)
    reservation.delete()
    return redirect(reverse('list'))


@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    if request.user != reservation.user and not request.user.is_staff:
        raise PermissionDenied("403..You need to be the owner or staff to edit this reservation")

    if request.method == 'POST':
        form = ReserveTableForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been updated successfully.')
            return HttpResponseRedirect(reverse('list'))
    else:
        form = ReserveTableForm(instance=reservation)

    context = {'form': form}
    return render(request, 'edit_reservation.html', context)