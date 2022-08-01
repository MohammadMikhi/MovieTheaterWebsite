from django.db import models

# Create your models here.

class Movies(models.Model):
    name= models.CharField(max_length=100)
    posterURL= models.TextField()
    description=models.TextField(default="desc")
    def __str__(self):
        return self.name
