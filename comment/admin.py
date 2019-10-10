from django.contrib import admin
from .models import Comment
# Register your models here.


# Register your models here.
@admin.register(Comment)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['owner', 'belongproduct', 'content', 'reply']
    list_filter = ['created']
