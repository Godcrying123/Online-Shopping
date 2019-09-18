from rest_framework import serializers

from .models import Order, OrderItem
from product.serializer import ProductSerializer
from user.models import Users
from product.models import Product
from user.serializers import BuyerSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name']


class OrderItemSerializer(serializers.ModelSerializer):
    boughtproducts = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'boughtproducts', 'quantity', 'price', 'status_delivery']


class OrderSerializer(serializers.ModelSerializer):
    ownorders = BuyerSerializer(read_only=True)
    orderitems = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'ownorders', 'status_order', 'created', 'orderitems']


class OrderByUserNameSerializer(serializers.ModelSerializer):
    ownorders = OrderSerializer(read_only=True)

    class Meta:
        model = Users
        fields = ['id', 'username', 'ownorders']
