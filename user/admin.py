from django.contrib import admin
from .models import Buyer, Users
# Register your models here.

@admin.register(Buyer)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'mail', 'password', 'telephone', 'created_time', 'status_vip', 'status_user', 'recaddress']
    list_filter = ['created_time', 'status_vip', 'status_user']
    list_editable = ['status_vip', 'status_user']


@admin.register(Users)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'mail', 'password', 'telephone', 'created_time', 'recaddress']
    list_filter = ['created_time']
