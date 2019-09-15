from rest_framework import serializers

from .models import Order, OrderItem
from product.models import Product

from user.models import Users


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    boughtproducts = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'boughtproducts', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer()

    class Meta:
        model = Order
        fields = ['id', 'owner', 'status_order', 'status_delivery', 'created', 'orderitems']


class OrderByUserNameSerializer(serializers.ModelSerializer):
    ownorders = OrderSerializer(read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'username', 'ownorders']
