from django.urls import path
from . import apis

urlpatterns = [
    # order apis
    path('order/createorder/', apis.OrderCreate.as_view()),
    # path('order/createorupdate/<int:pk>/', apis.OrderDetail.as_view()),
    path('order/detail/<int:pk>/', apis.OrderItemDetail.as_view()),
    path('order/user/list/<int:pk>/', apis.OrderListByUser.as_view()),
]
