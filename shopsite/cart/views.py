from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.decorators.http import require_POST

from cart.forms import CartAddProductForm
from product.models import Product
from .cart import Cart
from django.views.decorators.cache import cache_page

# Create your views here.


class CartDetail(generic.ListView):
    template_name = 'cart/cart_detail.html'

    def get(self, request):
        username = request.get_signed_cookie('username', default=None, salt=settings.COOKIE_SALT_VALUE,
                                             max_age=settings.COOKIE_EXPIRE_TIME)
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
        return render(request, self.template_name, {'cart': cart, 'haslogged': username})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    # print(product)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

