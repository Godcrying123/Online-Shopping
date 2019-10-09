from django.shortcuts import render,get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views import View
from user.models import Users
# Create your views here.
# Create your views here.


class ordercreate(View):
    template_name = 'order/ordercreate.html'
    orderownerlist = []

    def orderownerchange(self, userid):
        if len(self.orderownerlist) != 0:
            self.orderownerlist.clear()
        self.orderownerlist.append(userid)
        print(self.orderownerlist)

    def get(self, request, *args, **kwargs):
        ownerid = kwargs.get('pk')
        ownerinstance = get_object_or_404(Users, pk=ownerid)
        self.orderownerchange(ownerid)
        print(ownerinstance.name)
        print(ownerinstance.mail)
        print(ownerinstance.telephone)
        print(ownerinstance.recaddress)
        ordercreateform = OrderCreateForm(initial={'receiver': ownerinstance.name, 'email': ownerinstance.mail,
                                                   'telephone': ownerinstance.telephone,
                                                   'address': ownerinstance.recaddress})
        return render(request, self.template_name, {'ordercreateform': ordercreateform})

    def post(self, request, *args, **kwargs):
        order_create_form = OrderCreateForm(request.POST)
        if order_create_form.is_valid():
            cd = order_create_form.cleaned_data
            receiver = cd['receiver']
            email = cd['email']
            telephone = cd['telephone']
            address = cd['address']
        return render(request, self.template_name, )




