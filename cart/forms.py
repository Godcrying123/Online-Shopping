from django import forms
from product.models import Product


class ProductDetailForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'salesamount')


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
