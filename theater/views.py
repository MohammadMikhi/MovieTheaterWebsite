from random import choices
from django.shortcuts import redirect, render
from theater.models import Movies, Messages, Bookings, ShowingTimes
from .forms import CreateNewBooking
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

    return render(request, 'home.html', {"movies": Movies.objects.all(), "showingTimes": ShowingTimes.objects.all()})


def bookings(response):
    pass


def aboutus(response):
    pass


def addBooking(response, movie_id):
    movie= Movies.objects.get(id=movie_id)
    times= ShowingTimes.objects.filter(movie__name=movie).only('time')
    if response.method == 'POST':
        form = CreateNewBooking(response.POST,times)
        if form.is_valid():
            print(response.POST)
            form.save()
        return redirect('/home/')
    else:
        form = CreateNewBooking(times)

    return render(response, 'addBooking.html', {'form': form})
