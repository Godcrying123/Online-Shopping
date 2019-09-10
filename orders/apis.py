from rest_framework import generics
from rest_framework.response import Response

from .seralizers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem


class OrderList(generics.ListCreateAPIView):
    """
    General Method for listing and creating category instance
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateAPIView):
    """
    General Method for listing and creating category instance
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemDetail(generics.ListCreateAPIView):
    """
    General Method for listing and creating category instance
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
