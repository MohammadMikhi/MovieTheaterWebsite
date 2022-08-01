from logging import PlaceHolder
from django import forms

class CreateNewBooking(forms.Form):
    fname= forms.CharField(max_length=50, label="First Name")
    lname= forms.CharField(max_length=50, label="Last Name")
    email= forms.EmailField()
    times=forms.ChoiceField(choices=[('1:00', '1:00'), ('2:00','2:00')],label="Showing Times")
    movieClass=forms.CharField(label='Movie Class', widget=forms.RadioSelect(choices=[('economy','Economy'), ('first class', 'First Class')]))
    payment=forms.CharField(label='Payment Method', widget=forms.RadioSelect(choices=[('cash','Cash'), ('credit', 'Credit Card')]))
    subscribe= forms.BooleanField(required=False, label="Subscribe to our email service")
    