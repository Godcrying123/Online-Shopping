from django.db import models
from user.models import Users
from product.models import Product
# Create your models here.


class Comments(models.Model):
    owner = models.ForeignKey(Users, related_name='whoscomments',
                              verbose_name='comment_owner', on_delete=models.CASCADE)
    belongproduct = models.ForeignKey(Product, related_name='forwhichproduct',
                                      verbose_name='itemscomments', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='comment_content', editable=False, blank=False)
    reply = models.ForeignKey('self', verbose_name='parent_comment', related_name='children_replies',
                              blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created', )
        verbose_name = 'comments'
