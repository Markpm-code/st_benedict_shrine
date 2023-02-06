from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index.html'),
     path('about/',views.about, name='about.html'),
    path('gallery/',views.gallery, name='gallery.html'),
    path('services/', views.services, name='services.html')
]
