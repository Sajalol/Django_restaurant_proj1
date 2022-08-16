from . import views
from django.urls import path,include
from bar import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='home'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('reservation', views.ReservationList.as_view(), name='reservation')    
]