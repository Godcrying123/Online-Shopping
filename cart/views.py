from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.decorators.http import require_POST

from .cart import Cart
from product.models import Product
from product.forms import CartAddProductForm
# Create your views here.


class CartDetail(generic.ListView):
    template_name = 'cart/cart_detail.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        print(cart.cart8)
        return render(request, self.template_name, {'cart': cart})

    def post(self, request):

        return render(request, self.template_name, )
