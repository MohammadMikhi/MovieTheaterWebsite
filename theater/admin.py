from django.contrib import admin
from .models import Bookings, Messages, Movies, emailSubscribers
# Register your models here.
admin.site.register(Movies)
admin.site.register(Messages)
admin.site.register(emailSubscribers)
admin.site.register(Bookings)