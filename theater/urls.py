from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('bookings/',views.bookings, name="bookings"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('', views.home, name="home"),
    path('addBooking/<int:movie_id>', views.addBooking, name="addBooking")
]
