from django.http import Http404

from rest_framework import serializers

from .models import Order, OrderItem
from user.models import Users
from product.serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'owner', 'status_order', 'status_delivery', 'created', 'updated']


class OrderByUserNameSerializer(serializers.ModelSerializer):
    orderowner = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'username', 'orderowner']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'price', 'quantity']
