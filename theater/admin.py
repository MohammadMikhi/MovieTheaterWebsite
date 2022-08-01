from django.contrib import admin
from .models import Messages, Movies
# Register your models here.
admin.site.register(Movies)
admin.site.register(Messages)