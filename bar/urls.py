from . import views
from django.urls import path, include
from bar import views

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='home'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('reservation', views.reserve_table, name='reservation'),
    path('list_view', views.list_view, name='list'),
    path('detail_view/<reservation_id>', views.detail_view, name='detail'),
    path('delete_view/<int:reservation_id>', views.delete_view, name='delete'), 
    path('edit_reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('user_reservations/', views.user_reservations, name='user_reservations'),
]