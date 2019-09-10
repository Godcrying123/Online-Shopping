from django.urls import path
from . import apis

urlpatterns = [
    # order apis
    path('order/createorupdate/', apis.OrderList.as_view()),
    path('order/createorupdate/<int:pk>/', apis.OrderDetail.as_view()),
    path('order/item/detail/', apis.OrderItemDetail.as_view()),
]