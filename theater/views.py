from django.shortcuts import render

from theater.models import Movies

# Create your views here.
def home(response):
    return render(response, 'home.html',{"movies": Movies.objects.all() })
def bookings(response):
    pass
def aboutus(response):
    pass
