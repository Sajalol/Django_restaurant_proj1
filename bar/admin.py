from django.contrib import admin
from .models import Restaurant, Customer, Table, Reservation, Menu
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'country')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
     list_display = ('email', 'first_name', 'last_name')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('seats', 'min_people', 'max_people')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_filter = ('user','phone', 'number_of_guests', 'date', 'time', 'approved','seats')
    list_display = ('user','phone', 'number_of_guests', 'date', 'time', 'approved','seats')
    actions = ['approve_Reservation']

    def approve_Reservation(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):
    list_display = ('nameOfFood', 'meat', 'allergy', 'details', 'price')

    summernote_fields = ('details')