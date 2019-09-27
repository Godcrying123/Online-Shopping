from django.contrib import admin
from .models import Category,Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent_category', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['parent_category']
    list_editable = ['parent_category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available', 'price']


# @admin.register(CateProd)
# class CateProdAdmin(admin.ModelAdmin):
#     list_display_links = ['category', 'product']
#     list_display = ['category', 'product']
#     # list_editable = ['category', 'product']
