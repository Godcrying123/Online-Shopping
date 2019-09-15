from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'status_order', 'status_delivery', 'created', 'updated']
    list_filter = ['owner', 'status_order', 'status_delivery', 'created', 'updated']
    list_editable = ['status_order', 'status_delivery']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity']
