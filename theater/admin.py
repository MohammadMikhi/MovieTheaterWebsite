from django.contrib import admin
from .models import Bookings, Messages, Movies, ShowingTimes
# Register your models here.
admin.site.register(Movies)
admin.site.register(Messages)
admin.site.register(Bookings)
admin.site.register(ShowingTimes)