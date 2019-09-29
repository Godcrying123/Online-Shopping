from django.shortcuts import render, get_object_or_404
from django.views import generic
# Create your views here.


class CartDetail(generic.ListView):
    template_name = 'cart/cart_detail.html'
    # template_name = 'product/productdetail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,)

    def post(self, request):
        return render(request, self.template_name, )
