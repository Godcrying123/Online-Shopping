from django.http import Http404
from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins

from .serializer import ProductSerializer, CategorySerializer
from .models import Category, Product


class AllCategoryAllProductList(generics.ListAPIView):
    """
    All categories details
    """
    queryset = Category.objects.filter(Q(parent_category=None))
    serializer_class = CategorySerializer


class ProductList(generics.ListCreateAPIView):
    """
    General Method for listing and creating product instance
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AdminProductDetail(generics.ListAPIView):
    """
    the product details
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListByCategory(generics.ListAPIView):
    """
    all product list in the sub categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        print(self.request.META)
        return self.retrieve(request, *args, **kwargs)

    def get_object(self, cate1ID, cate2ID):
        return None
        # try:
        #     return Category.objects.get(name=category)
        # except Category.DoesNotExist:
        #     raise Http404

    def retrieve(self, request, *args, **kwargs):
        return None
        # instance = self.get_object(category)
        # serializer = self.get_serializer(instance)
        # return Response(serializer.data)
