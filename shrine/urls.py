from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index.html'),
    path('our_story/',views.our_story, name='our_story.html'),
    path('gallery/',views.gallery, name='gallery.html'),
    path('services/', views.services, name='services.html'),
#    path('login/', views.login, name='account_login')
]
