from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('category/products/<slug:categoryslug>/', views.CategoryProductList.as_view(),
         name='category_product_list_by_category'),
    path('category/products/', views.CategoryProductList.as_view(), name='all_category_product_list'),
    path('category/products/detail/<int:pk>/', cache_page(5 * 60)(views.ProductListDetail.as_view()), name='product_detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
