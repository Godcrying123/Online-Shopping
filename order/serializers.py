from rest_framework import serializers

from .models import Order, OrderItem
from product.serializers import ProductSerializer
from user.models import Users


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price', 'status_delivery']


class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'status_order', 'created', 'orderitems']


class OrderByUserNameSerializer(serializers.ModelSerializer):
    own_orders = OrderSerializer(many=True)

    class Meta:
        model = Users
        fields = ['id', 'name', 'username', 'own_orders']

