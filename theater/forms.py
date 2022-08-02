from django import forms
from .models import Bookings
class CreateNewBooking(forms.ModelForm):
    name= forms.CharField(max_length=100, label="Name")
    email= forms.EmailField()
    showingTime=forms.ChoiceField(choices=[('13:00:00', '1:00'), ('14:00:00','2:00')],label="Showing Times")
    bookingClass=forms.CharField(label='Movie Class', widget=forms.RadioSelect(choices=[('economy','Economy'), ('first class', 'First Class')]))
    paymentMethod=forms.CharField(label='Payment Method', widget=forms.RadioSelect(choices=[('cash','Cash'), ('credit', 'Credit Card')]))
    
    class Meta:
        model= Bookings
        fields=['name', 'email', 'showingTime', 'bookingClass', 'paymentMethod']

    