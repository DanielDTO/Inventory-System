from django import forms
from .models import *


class desktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('Date','Name', 'Price', 'Category', 'Quantity', 'Status')

class laptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('Date','Name', 'Price', 'Category', 'Quantity', 'Status')

class mobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('Date','Name', 'Price', 'Category', 'Quantity', 'Status')

class stationaryForm(forms.ModelForm):
    class Meta:
        model = Stationary
        fields = ('Date', 'Name', 'Price', 'Category', 'Quantity', 'Status')

