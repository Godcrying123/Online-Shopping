from django.db import models
from product.models import Product
from comment.models import Comments
from user.models import Users
# Create your models here.


class Images(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=40)
    product_img = models.ForeignKey(Product, null=True, on_delete=models.CASCADE,
                                    verbose_name='product_image', related_name='belongstoimg')
    comment_img = models.ForeignKey(Comments, null=True, on_delete=models.CASCADE,
                                    verbose_name='comment_image', related_name='belongstocom')
    user_img = models.ForeignKey(Users, null=True, on_delete=models.CASCADE,
                                 verbose_name='user_image', related_name='belongstouser')
    image = models.ImageField(upload_to='image/', blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'images'
