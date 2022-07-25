from django.contrib import admin
from .models import Restaurant, Customer, Table, Reservation, Menu
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Customer)
admin.site.register(Table)
admin.site.register(Reservation)

@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    summernote_fields = ('Menu')