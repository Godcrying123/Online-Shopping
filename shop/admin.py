from django.contrib import admin
from .models import Store

# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_name', 'store_location', 'status', 'created_time']
    list_filter = ['created_time', 'status', 'store_location']
    list_editable = ['status', 'store_location']