from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import apis, authViews


urlpatterns = [
    # buyer views
    path('buyers/', apis.BuyerList.as_view()),
    path('admin/buyers/', apis.AdminBuyerList.as_view()),
    path('admin/buyers/<int:pk>/', apis.AdminBuyerDetail.as_view()),
    path('buyers/<str:username>/', apis.BuyerDetailByName.as_view()),
    path('v1/auth/', authViews.AuthView.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
