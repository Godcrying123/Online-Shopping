from django.urls import path
from . import apis

urlpatterns = [
    # order apis
    path('order/createorder/', apis.OrderList.as_view()),
    # path('order/createorupdate/<int:pk>/', apis.OrderDetail.as_view()),
    path('order/detail/', apis.OrderItemDetail.as_view()),
    # path('order/<str:username>/orderlist/', apis.OrderListByUser.as_view()),
]