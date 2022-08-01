from email import message
from django.db import models

# Create your models here.

class Movies(models.Model):
    name= models.CharField(max_length=100)
    posterURL= models.TextField()
    description=models.TextField(default="")
    def __str__(self):
        return self.name

class Messages(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name