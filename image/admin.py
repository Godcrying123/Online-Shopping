from django.contrib import admin
from .models import Images


# Register your models here.
@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'product_img', 'comment_img', 'user_img', 'created', 'updated']
    list_filter = ['created', 'updated']
