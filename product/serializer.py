from rest_framework import serializers

from .models import Category, Product


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'description', 'price', 'available', 'created', 'updated',
                  'onstock', 'salesamount']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price', 'available', 'salesamount']


class CategorySerializer2(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']


class CategorySerializer(serializers.ModelSerializer):
    children_categories = CategorySerializer2(many=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'children_categories', 'products']


class CategoryProductSerialzer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']





