from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/<int:pk>/', views.payment_process, name='payment_process'),
    path('done/', views.payment_done, name='payment_done'),
    path('canceled/', views.payment_canceled, name='payment_canceled'),
]