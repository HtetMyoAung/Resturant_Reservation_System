from django.urls import path
from . import views

urlpatterns = [

    path('create/', views.create_reservation, name='create_reservation'),
    path('success/', views.reservation_success, name='reservation_success'),
]
