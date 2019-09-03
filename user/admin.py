from django.contrib import admin
from user.models import Buyer
# Register your models here.
@admin.register(Buyer)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'mail', 'password', 'telephone', 'created_time', 'recaddress', 'status_vip', 'status_user']
    list_filter = ['created_time', 'status_vip', 'status_user']
    list_editable = ['mail', 'recaddress', 'status_vip', 'status_user']