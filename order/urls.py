from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    # order views
    path('detail/preview/', views.orderpreview.as_view(), name='order_preview'),
    path('detail/preview/<str:userinfo>/', views.orderpreview.as_view(), name='order_preview'),
    path('create', views.ordercreate.as_view(), name='order_create'),
    path('detail/review/<int:pk>/', views.orderreview.as_view(), name='order_review'),
    path('list/<int:pk>/', views.orderlist.as_view(), name='order_list'),
]