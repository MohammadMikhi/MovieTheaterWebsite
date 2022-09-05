from django.http import HttpResponse
from django.shortcuts import redirect, render
from theater.models import Movies, Messages, ShowingTimes, Bookings
from .forms import CreateNewBooking, searchBooking
# Create your views here.


def home(request):
    return render(request, 'home.html', {"movies": Movies.objects.all()})


def newMessage(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        Messages.objects.create(
            name=name,
            email=email,
            message=message
        )
        success= name
        return HttpResponse(success)


def searchBookings(response):
    if response.method == "POST":
        form = searchBooking(response.POST)

        if form.is_valid():
            e = form.cleaned_data['email']
            booking = Bookings.objects.filter(email=e)
    else:
        form = searchBooking()
        booking = Bookings.objects.filter(email="").first
    print(booking)
    return render(response, 'searchBookings.html', {'form': form, 'booking': booking})


def listOfMovies(response):
    pass


def addBooking(response, movie_id):
    movie = Movies.objects.get(id=movie_id)
    times = ShowingTimes.objects.filter(movie__name=movie).only('time')
    if response.method == 'POST':
        form = CreateNewBooking(times, response.POST)
        if form.is_valid():
            print(response.POST)
            form.save()
        return redirect('/home/')
    else:
        form = CreateNewBooking(times)

    return render(response, 'addBooking.html', {'form': form})
