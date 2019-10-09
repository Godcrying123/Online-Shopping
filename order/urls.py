from django.urls import path
from order.views import ordercreate


app_name = 'order_view'

urlpatterns = [
    # order views
    path('create/<int:pk>/', ordercreate.as_view(), name='order_create'),
]