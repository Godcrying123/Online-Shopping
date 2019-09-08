from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views, authViews


urlpatterns = [
    # buyer views
    path('buyers/', views.BuyerList.as_view()),
    path('buyers/<int:pk>/', views.BuyerDetail.as_view()),
    path('buyers/<str:username>/', views.BuyerDetailByName.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('v1/auth/', authViews.AuthView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)