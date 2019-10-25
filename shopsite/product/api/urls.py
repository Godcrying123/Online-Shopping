from django.urls import path
from product.api import apis

app_name = 'product_api'

urlpatterns = [
    #category apis
    path('categories/products/', apis.AllCategoryAllProductList.as_view()),
    # re_path(r'categories/(?P<cate1ID>\w+)/(?P<cate2ID>\w+)/', apis.ProductListByCategory.as_view),
    path('categories/<int:pk>/', apis.ProductListByCategory.as_view()),
    # path('categories/<int:cate1ID>/<int:cate2ID>/', apis.ProductListByCategory.as_view()),
    path('categories/products/<int:pk>/', apis.ProductDetail.as_view()),
    path('products/create/', apis.ProductList.as_view())
]