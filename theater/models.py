from django.db import models

# Create your models here.


class Movies(models.Model):
    name = models.CharField(max_length=100)
    posterURL = models.URLField()
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Bookings(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    showingTime = models.CharField(max_length=50, choices=[
                                   ('13:00:00', '1:00'), ('14:00:00', '2:00')])
    bookingClass = models.CharField(max_length=100, choices=[(
        'economy', 'Economy'), ('first class', 'First Class')])
    paymentMethod = models.CharField(max_length=100, choices=[
                                     ('cash', 'Cash'), ('credit', 'Credit Card')])

    def __str__(self):
        return self.name


class ShowingTimes(models.Model):
    time = models.TimeField()
    movieName = models.CharField(max_length=100)
    capacity = models.DecimalField(max_digits=99, decimal_places=3)

    def __str__(self):
        return str(self.time)
