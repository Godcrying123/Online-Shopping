from django.contrib import admin
from .models import Comments
# Register your models here.


# Register your models here.
@admin.register(Comments)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['owner', 'belongproduct', 'content', 'reply']
    list_filter = ['created']
