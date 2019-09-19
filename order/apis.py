from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins

from .serializers import OrderSerializer, OrderItemSerializer, OrderByUserNameSerializer, ProductSerializer
from .models import Order, OrderItem
from product.models import Product
from user.models import Users


class OrderCreate(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    create a order
    """
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        owner_id = self.request.data.get('owner')
        products = self.request.data.get('products')
        user = Users.objects.get(pk=owner_id)
        ordercreated = Order.objects.create(owner=user)
        for orderproduct in products:
            product_id = orderproduct.get('id')
            quantity = orderproduct.get('quantity')
            price = orderproduct.get('price')
            product = Product.objects.get(pk=product_id)
            orderitem = OrderItem.objects.create(order=ordercreated, product=product, quantity=quantity, price=price)
            print(orderitem)
            serializer = self.get_serializer(orderitem)
        return Response(serializer.data)


class OrderListByUser(generics.RetrieveAPIView):
    """
    Listing all order details for specific user
    """
    queryset = Users.objects.all()
    serializer_class = OrderByUserNameSerializer

    # def get(self, request, username, *args, **kwargs):
    #     return self.retrieve(request, username, *args, **kwargs)
    #
    # def get_object(self, username):
    #     try:
    #         return Users.objects.get(username=username)
    #     except Users.DoesNotExist:
    #         raise Http404
    #
    # def retrieve(self, request, username, *args, **kwargs):
    #     instance = self.get_object(username)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


class OrderItemDetail(generics.RetrieveUpdateAPIView):
    """
    order detail list
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    # def create(self, request, *args, **kwargs):
    #     user_username_for_order = self.request.data.get('owner.username')
    #     user_instance = Users.objects.get(username=user_username_for_order)
    #     serializer = OrderItemSerializer(user_instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
