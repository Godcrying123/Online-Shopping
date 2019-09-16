from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import apis, authViews


urlpatterns = [
    # buyer views
    path('register/', apis.BuyerList.as_view()),
    # path('admin/buyers/', apis.AdminBuyerList.as_view()),
    # path('admin/buyers/<int:pk>/', apis.AdminBuyerDetail.as_view()),
    path('profile/detail/<int:pk>/', apis.BuyerDetailByName.as_view()),
    path('login/', authViews.AuthView.as_view()),
    path('register/valuecheck/<str:fieldname>/<str:fieldvalue>', apis.UserRegisterCheck.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
