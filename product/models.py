from django.db import models
from django.http import Http404
from django.db.models import Q

from shop.models import Store

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField('slug', max_length=40)
    parent_category = models.ForeignKey('self', verbose_name='parent_category', related_name='children_categories', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'

    def __str__(self):
        return self.name

    def firstlevelcategory(self):
        return Category.objects.filter(Q(parent_category=None))

    def secondlevelcategory(self):
        return Category.objects.filter(Q(parent_category=self))

    def categoryproductlist(self):
        return Product.objects.filter(Q(category=self))

    def numofproductincategory(self):
        return len(Product.objects.filter(Q(category=self)))


class Product(models.Model):
    # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='products', verbose_name='category_product')
    # store = models.ForeignKey(Store, related_name='stores', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    onstock = models.PositiveIntegerField(default=0)
    salesamount = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    # def product_available(self):
    #     if Product.objects.


