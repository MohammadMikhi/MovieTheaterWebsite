from asyncio.windows_events import NULL
from turtle import title
from django import forms
from .models import Bookings
class CreateNewBooking(forms.ModelForm):
    
    def __init__(self, time_list, *args, **kwargs):
        super(CreateNewBooking, self).__init__(*args, **kwargs)
        self.fields['showingTime'] = forms.ChoiceField(choices=tuple([(str(time), str(time)) for time in time_list]), label="Showing time")
    
    name= forms.CharField(max_length=100, label="Name")
    email= forms.EmailField()
    bookingClass=forms.CharField(label='Movie Class', widget=forms.RadioSelect(choices=[('economy','Economy'), ('first class', 'First Class')]))
    paymentMethod=forms.CharField(label='Payment Method', widget=forms.RadioSelect(choices=[('cash','Cash'), ('credit', 'Credit Card')]))
    
    class Meta:
        model= Bookings
        fields=['name', 'email', 'showingTime', 'bookingClass', 'paymentMethod']

    
class searchBooking(forms.Form):
    email= forms.EmailField()
     
    