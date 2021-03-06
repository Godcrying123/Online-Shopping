from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from shop.models import Store


# Create your models here.


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('name'), max_length=200, unique=True),
        slug=models.SlugField(_('slug'), max_length=40)
    )
    parent_category = models.ForeignKey('self', verbose_name='parent_category', related_name='children_categories', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

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

    def get_absolute_url(self):
        return reverse('product:category_product_list_by_category', args=[self.slug])


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_('name'), max_length=200, db_index=True),
        description=models.TextField(_('description'), blank=True)
    )
    # category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='products', verbose_name='category_product')
    store = models.ForeignKey(Store, related_name='sold_products', on_delete=models.CASCADE, verbose_name='own_store',
                              blank=True, default=None)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    onstock = models.PositiveIntegerField(default=0)
    salesamount = models.PositiveIntegerField(default=0)

    class Meta:
        # ordering = ('name', )
        verbose_name = 'product'

    def __str__(self):
        return self.name

    def categorynameforproduct(self):
        return self.category.all()

    def get_absolute_url(self):
        return reverse('product:product_detail',  args=[self.id])

    # def product_available(self):
    #     if Product.objects.



