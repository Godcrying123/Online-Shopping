from django import forms
from .models import Order


class OrderCreateForm(forms.Form):
    receiver = forms.CharField(label='Receiver Name', max_length=100, required=True)
    email = forms.EmailField(label='Receiver E-mail', max_length=100, required=True)
    telephone = forms.CharField(label='Receiver Telephone', max_length=100, required=True)
    postal = forms.CharField(label='Receiver Address Postal', max_length=100, required=False)
    address = forms.CharField(label='Receiver Address', max_length=100, required=True)