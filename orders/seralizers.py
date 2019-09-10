from rest_framework import serializers

from .models import Order, OrderItem
from user.serializers import UsersSerializer
from product.serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'status_order', 'status_delivery', 'created', 'updated']


class OrderItemSerializer(serializers.ModelSerializer):
    owner = UsersSerializer()
    orderitems = OrderSerializer()
    # products = ProductSerializer(many=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'owner', 'orderitems']

