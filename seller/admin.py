from django.contrib import admin
from .models import Seller
# Register your models here.


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'mail', 'password', 'created_time', 'delivery_out_address', 'status']
    list_filter = ['created_time', 'status']
    list_editable = ['mail', 'delivery_out_address', 'status']
