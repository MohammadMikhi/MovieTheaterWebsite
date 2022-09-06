from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('searchBookings/', views.searchBookings, name="searchBookings"),
    path('', views.home, name="home"),
    path('addBooking/<int:movie_id>', views.addBooking, name="addBooking"),
    path('newMessage/', views.newMessage, name="newMessage"),
]
