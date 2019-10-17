from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import Store
from user.models import User


# Create your models here.


class Seller(User):
    STATUS_ITEMS = (
        {'normal', _('Normal')},
        {'delete', _('Deleted')},
        {'banned', _('Banned')},
        {'vip', 'VIP'},
    )
    status = models.CharField(default='normal', max_length=100, choices=STATUS_ITEMS, verbose_name='store_status')
    store = models.ManyToManyField(Store, related_name='owners', verbose_name='own_stores')
    # delivery_out_address = models.CharField(max_length=200, db_index=True, verbose_name='delivery_out_address')

    def __str__(self):
        return self.username

