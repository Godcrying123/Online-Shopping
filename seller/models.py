from django.db import models
from user.models import User
from shop.models import Store

# Create your models here.


class Seller(User):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_BANNED = 2
    STATUS_VIP = 3
    STATUS_ITEMS = (
        {STATUS_NORMAL, 'normal'},
        {STATUS_DELETE, 'deleted'},
        {STATUS_BANNED, 'banned'},
        {STATUS_VIP, 'VIP'},
    )
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='status')
    store = models.ManyToManyField(Store, related_name='sellers_stores')
    delivery_out_address = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.username

