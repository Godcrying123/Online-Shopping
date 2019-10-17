from django.contrib import admin

from buyer.models import Buyer
from .models import User, UserInfoEntity


# Register your models here.

@admin.register(Buyer)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'mail', 'password', 'telephone', 'created_time', 'status_vip', 'status_user']
    list_filter = ['created_time', 'status_vip', 'status_user']
    list_editable = ['status_vip', 'status_user']


class UserInfoEntityInline(admin.TabularInline):
    model = UserInfoEntity
    raw_id_fields = ['owner']


@admin.register(User)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'mail', 'password', 'telephone', 'created_time']
    list_filter = ['created_time']
    inlines = [UserInfoEntityInline]
