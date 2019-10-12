from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    # order views
    path('detail/preview/', views.orderpreview.as_view(), name='order_preview'),
    path('detail/preview/<str:userinfo>/', views.orderpreview.as_view(), name='order_preview'),
    path('create', views.ordercreate.as_view(), name='order_create'),
    path('detail/review/<int:pk>/', views.orderreview.as_view(), name='order_review'),
    path('list/', views.orderlist.as_view(), name='order_list'),
    # path('export/csv', views.orderlist.as_view(), name='order_list'),
    path('print/pdf/<int:pk>/', views.print_to_pdf, name='print_PDF'),
]