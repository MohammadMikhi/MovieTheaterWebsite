from email import message
import email
from urllib import request
from django.shortcuts import render

from theater.models import Movies, Messages, emailSubscribers, Bookings

# Create your views here.


def home(request):
    if request.method == 'POST':
        if 'messageSubmit' in request.POST:
            name1 = request.POST['name']
            message1 = request.POST['message']
            email1 = request.POST['email']
            newMessage = Messages(name=name1, message=message1, email=email1)
            newMessage.save()
        elif 'bookingSubmit' in request.POST:
            name1=request.POST['fname'] + " " + request.POST['lname']
            email1 = request.POST['email']
            time=request.POST['times']
            class1=request.POST['movieClass']
            payment=request.POST['payment']
            sub=request.POST['subscribe']
            newBooking=Bookings(name=name1, email=email1, showingTime=time, bookingClass=class1, paymentMethod=payment)
            if sub=='subscribe':
                newSubscriber=emailSubscribers(name=name1, email=email1)
                newSubscriber.save()
            newBooking.save()

    return render(request, 'home.html', {"movies": Movies.objects.all()})


def bookings(response):
    pass


def aboutus(response):
    pass
