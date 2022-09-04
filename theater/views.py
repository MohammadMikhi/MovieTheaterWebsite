from time import time
from django.shortcuts import redirect, render
from theater.models import Movies, Messages, ShowingTimes, Bookings
from .forms import CreateNewBooking, searchBooking
# Create your views here.


def home(request):
    if request.method == 'POST':
        if 'messageSubmit' in request.POST:
            name1 = request.POST['name']
            message1 = request.POST['message']
            email1 = request.POST['email']
            newMessage = Messages(name=name1, message=message1, email=email1)
            newMessage.save()
    """
        elif 'bookingSubmit' in request.POST:
            name1 = request.POST['fname'] + " " + request.POST['lname']
            email1 = request.POST['email']
            time = request.POST['times']
            class1 = request.POST['movieClass']
            payment = request.POST['payment']
            newBooking = Bookings(name=name1, email=email1, showingTime=time,
                                  bookingClass=class1, paymentMethod=payment)
            newBooking.save()
    """

    return render(request, 'home.html', {"movies": Movies.objects.all()})


def searchBookings(response):
    if response.method == "POST":
        form= searchBooking(response.POST)
        
        if form.is_valid():
            e= form.cleaned_data['email']
            booking= Bookings.objects.filter(email=e)
    else:
        form= searchBooking()
        booking=Bookings.objects.filter(email="").first
    print(booking)
    return render(response, 'searchBookings.html',{'form': form, 'booking': booking})


def listOfMovies(response):
    pass


def addBooking(response, movie_id):
    movie= Movies.objects.get(id=movie_id)
    times= ShowingTimes.objects.filter(movie__name=movie).only('time')
    if response.method == 'POST':
        form = CreateNewBooking(times, response.POST)
        if form.is_valid():
            print(response.POST)
            form.save()
        return redirect('/home/')
    else:
        form = CreateNewBooking(times)

    return render(response, 'addBooking.html', {'form': form})
