from rest_framework import generics

from product.api.serializers import ProductSerializer, CategorySerializer, CategoryProductSerialzer, ProductDetailSerializer
from product.models import Category, Product


class AllCategoryAllProductList(generics.ListAPIView):
    """
    All categories details
    """
    queryset = Category.firstlevelcategory(Category)
    serializer_class = CategorySerializer


class ProductList(generics.ListCreateAPIView):
    """
    General Method for listing and creating product instance
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    """
    the product details
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductListByCategory(generics.RetrieveAPIView):
    """
    all product list with a specific category id
    """
    queryset = Category.objects.all()
    serializer_class = CategoryProductSerialzer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    #
    # def get_object(self, cate1ID, cate2ID):
    #     if cate2ID is None:
    #         try:
    #             return Category.objects.get(pk=cate1ID)
    #         except Category.DoesNotExist:
    #             raise Http404
    #
    # def retrieve(self, request, *args, **kwargs):
    #     cate1ID = kwargs.get('cate1ID')
    #     cate2ID = kwargs.get('cate2ID', None)
    #     instance = self.get_object(cate1ID,cate2ID)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
