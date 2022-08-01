from email import message
import email
from django.db import models

# Create your models here.

class Movies(models.Model):
    name= models.CharField(max_length=100)
    posterURL= models.URLField()
    description=models.TextField(default="")
    def __str__(self):
        return self.name

class Messages(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name
    
class emailSubscribers(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name
    
class Bookings(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    showingTime=models.CharField(max_length=25)
    bookingClass=models.CharField(max_length=100)
    paymentMethod=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    