from django.urls import path
from order.views import ordercreate, orderreceiver


app_name = 'order_view'

urlpatterns = [
    # order views
    # path('create/', orderreceiver.as_view(), name='order_create'),
    path('create/', ordercreate.as_view(), name='order_create'),
    path('create/<str:userinfo>/', ordercreate.as_view(), name='order_create'),
]