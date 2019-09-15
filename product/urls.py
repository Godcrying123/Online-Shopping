from django.urls import path, re_path

from rest_framework.urlpatterns import format_suffix_patterns

from . import apis

urlpatterns = [
    #category views
    path('categories/products/', apis.AllCategoryAllProductList.as_view()),
    # path('admin/categories/', apis.AdminCategoryList.as_view()),
    # re_path(r'categories/(?P<cate1ID>\w+)/(?P<cate2ID>\w+)/', apis.ProductListByCategory.as_view),
    path('categories/<int:pk>/', apis.ProductListByCategory.as_view()),
    # path('categories/<int:cate1ID>/<int:cate2ID>/', apis.ProductListByCategory.as_view()),
    # path('products/', apis.ProductList.as_view()),
    path('categories/products/<int:pk>/', apis.AdminProductDetail.as_view()),
    # path('<str:category>/products/', apis.ProductListByCategory.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
