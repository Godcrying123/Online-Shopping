from django.db import models
from django.db.models import Q

from product.models import Product
from comment.models import Comment
from user.models import User
# Create your models here.


class Images(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField('slug', max_length=40)
    product_img = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='belongstoProduct',
                                    related_name='product_images', null=True, blank=True)
    comment_img = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='belongstoComment',
                                    related_name='comment_images', null=True, blank=True)
    user_img = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='belongstoUser',
                                 related_name='user_images', null=True, blank=True)
    image = models.ImageField(upload_to='image/', blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'image'
        ordering = ('created', )

    def onlyonebelongs(self, *args):
        arg1 = args[0]
        arg2 = args[1]
        arg3 = args[2]
        if arg1 is not None and arg2 is None and arg3 is None:
            return True
        elif arg2 is not None and arg1 is None and arg3 is None:
            return True
        elif arg3 is not None and arg1 is None and arg2 is None:
            return True
        return False

    def save(self, *args, **kwargs):
        """
        check there each image only has one relationship with product, comment or users
        """
        product_img = self.product_img
        comment_img = self.comment_img
        user_img = self.user_img
        if not self.onlyonebelongs(product_img, comment_img, user_img):
            raise ValueError("it only allows one belongs entity for saving")
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, *args, **kwargs):
        """
        check there each image only has one relationship with product, comment or users
        """
        product_img = cls.product_img
        comment_img = cls.comment_img
        user_img = cls.user_img
        if not cls.onlyonebelongs(product_img, comment_img, user_img):
            raise ValueError("it only allows one belongs entity for saving")
        super().create(*args, **kwargs)

    def getallimagesforproduct(self, productinstance):
        return Images.objects.filter(Q(product_img=productinstance))





