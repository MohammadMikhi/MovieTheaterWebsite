from tkinter import CASCADE
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
    showingTime = models.CharField(max_length=50)
    bookingClass = models.CharField(max_length=100)
    paymentMethod = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ShowingTimes(models.Model):
    time = models.TimeField()
    movie = models.ForeignKey(Movies, blank=True, null=True, on_delete=models.CASCADE)
    capacity = models.DecimalField(max_digits=99, decimal_places=3)

    def __str__(self):
        return str(self.time)
