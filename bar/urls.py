from . import views
from django.urls import path, include
from bar import views
from .views import delete_view, list_view, detail_view

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='home'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('reservation', views.reserve_table, name='reservation'),
    path('delete_view', views.delete_view, name='delete'),
    path('list_view', views.list_view, name='list'),
    path('detail_view/<reservation_id>', views.detail_view, name='detail'), 
]