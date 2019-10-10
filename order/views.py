from django.shortcuts import render,get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views.generic import FormView
from django.views import View
from user.models import User
# Create your views here.


class ordercreate(View):
    template_name = 'order/ordercreate.html'
    # form_class = OrderCreateForm

    def get(self, request, *args, **kwargs):
        # ownerid = kwargs.get('pk')
        cart = Cart(request)
        ownerinstance = get_object_or_404(User, pk=3)

        # ordercreateform = OrderCreateForm(initial={'receiver': ownerinstance.name, 'email': ownerinstance.mail,
        #                                            'telephone': ownerinstance.telephone,
        #                                            'address': ownerinstance.recaddress})
        # self.get_form_kwargs(ownerinstance)
        ordercreateform = OrderCreateForm()
        return render(request, self.template_name, {'ordercreateform': ordercreateform,
                                                    'cart': cart, 'owner': ownerinstance})

    def post(self, request, *args, **kwargs):
        order_create_form = OrderCreateForm(request.POST)
        if order_create_form.is_valid():
            cd = order_create_form.cleaned_data
            receiver = cd['receiver']
            email = cd['email']
            telephone = cd['telephone']
            address = cd['address']
        return render(request, self.template_name, )


class orderreceiver(View):
    template_name = 'order/ordercreate.html'

    def get(self, request):
        return render(request, self.template_name, )

    def post(self, request):
        return render(request, self.template_name, )



