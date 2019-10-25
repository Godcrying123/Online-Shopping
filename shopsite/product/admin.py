from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'parent_category', 'created', 'updated']
    # prepopulated_fields = {'slug': ('name',)}
    list_filter = ['parent_category']
    list_editable = ['parent_category']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'description', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available', 'price']


# @admin.register(CateProd)
# class CateProdAdmin(admin.ModelAdmin):
#     list_display_links = ['category', 'product']
#     list_display = ['category', 'product']
#     # list_editable = ['category', 'product']
