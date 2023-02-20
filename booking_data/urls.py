from . import views
from django.urls import path

urlpatterns = [
    path('makebooking', views.booking, name='booking'),
    path('', views.Booking_dataList.as_view(), name='booking.html'),
]