from django.db import models
from seller.models import Seller
# Create your models here.


# class Post(models.Model):
#     title = models.CharField(max_length=200, db_index=True, verbose_name='title')
#     content = models.TextField(verbose_name='content')
#     created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')
#     seller = models.ForeignKey(Seller, related_name='seller_posts', on_delete=models.CASCADE)
#
#     class Meta:
#         ordering = ('title',)
#         verbose_name = 'post'
#         verbose_name_plural = 'posts'
