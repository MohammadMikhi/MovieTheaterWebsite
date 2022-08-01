from email import message
import email
from urllib import request
from django.shortcuts import render

from theater.models import Movies,Messages

# Create your views here.
def home(request):
    if request.method== 'POST':
        if 'messageSubmit' in request.POST: 
            name1=request.POST['name']
            message1=request.POST['message']
            email1=request.POST['email']
            newMessage= Messages(name=name1,message=message1,email=email1)
            newMessage.save()
       # elif 'bookingSubmit' in request.POST:
            
    return render(request, 'home.html',{"movies": Movies.objects.all() })
def bookings(response):
    pass
def aboutus(response):
    pass
