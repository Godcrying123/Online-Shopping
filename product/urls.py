from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import apis

urlpatterns = [
    #category views
    path('categories/', apis.CategoryList.as_view()),
    path('admin/categories/', apis.AdminCategoryList.as_view()),
]