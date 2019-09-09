from django.http import Http404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins

from .serializer import ProductSerializer, CategorySerializer, AdminCategorySerializer
from .models import Category


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

