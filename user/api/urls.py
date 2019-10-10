from django.urls import path
from user.api import apis, authViews

app_name = 'user_api'

urlpatterns = [
    # User API URL
    path('register/', apis.BuyerList.as_view()),
    path('profile/detail/<str:username>/', apis.BuyerDetailByName.as_view()),
    path('profile/detail/<int:pk>/', apis.BuyerDetailByID.as_view()),
    path('login/', authViews.AuthView.as_view()),
    path('register/valuecheck/<str:fieldname>/<str:fieldvalue>', apis.UserRegisterCheck.as_view()),
    # path('admin/buyers/', apis.AdminBuyerList.as_view()),
    # path('admin/buyers/<int:pk>/', apis.AdminBuyerDetail.as_view()),
]
