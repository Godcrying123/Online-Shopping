from django import forms
from .models import Product


class ProductDetailForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'salesamount')