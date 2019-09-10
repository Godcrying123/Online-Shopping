from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins

from .serializer import ProductSerializer, CategorySerializer, AdminCategorySerializer, ProductByCategorySerializer
from .models import Category, Product


class CategoryList(generics.ListCreateAPIView):
    """
    General Method for listing and creating category instances
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class AdminCategoryList(generics.ListCreateAPIView):
    """
    General Method for listing and creating an admin category instance
    """
    queryset = Category.objects.all()
    serializer_class = AdminCategorySerializer


class ProductList(generics.ListCreateAPIView):
    """
    General Method for listing and creating product instance
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AdminProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a product instance for admin user
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListByCategory(generics.ListAPIView):
    """
    General Method for listing and creating product instance with different category
    """
    serializer_class = ProductByCategorySerializer

    def get(self, request, category, *args, **kwargs):
        return self.retrieve(request, category, *args, **kwargs)

    def put(self, request, category, *args, **kwargs):
        return self.update(request, category, *args, **kwargs)

    def get_object(self, category):
        try:
            return Category.objects.get(name=category)
        except Category.DoesNotExist:
            raise Http404

    def retrieve(self, request, category, *args, **kwargs):
        instance = self.get_object(category)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

