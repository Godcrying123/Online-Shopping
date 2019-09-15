from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .seralizers import OrderSerializer, OrderItemSerializer, OrderByUserNameSerializer
from .models import Order, OrderItem
from user.models import Users


class OrderList(generics.CreateAPIView):
    """
    create a order
    """
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateAPIView):
    """
    General Method for listing and creating category instance
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListByUser(generics.ListAPIView):
    """
    General Method for listing and creating category instance by user
    """
    serializer_class = OrderByUserNameSerializer

    def get(self, request, username, *args, **kwargs):
        return self.retrieve(request, username, *args, **kwargs)

    def get_object(self, username):
        try:
            return Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise Http404

    def retrieve(self, request, username, *args, **kwargs):
        instance = self.get_object(username)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class OrderItemDetail(generics.ListAPIView):
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
