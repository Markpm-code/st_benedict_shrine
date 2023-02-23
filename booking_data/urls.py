from . import views
from django.urls import path

urlpatterns = [
    path('makebooking', views.booking, name='booking'),
    path('reservations/', views.ReservationList.as_view(), name='reservations'),
]