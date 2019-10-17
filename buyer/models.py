from django.db import models
from user.models import User

from django.utils.translation import gettext_lazy as _
# Create your models here.

class Buyer(User):
    STATUS_VIP = (
        ('vip', 'VIP'),
        ('not-vip', _('Not VIP')),
    )
    STATUS_USER = (
        ('normal', _('Normal')),
        ('deleted', _('Deleted')),
        ('banned', _('Banned')),
    )
    status_vip = models.CharField(default='not-vip', max_length=10,
                                  choices=STATUS_VIP, verbose_name='status_vip', db_index=True, blank=True)
    status_user = models.CharField(default='normal', max_length=10,
                                   choices=STATUS_USER, verbose_name='status_user', db_index=True, blank=True)
    # order = models.ForeignKey(Order, verbose_name='own_order', related_name='boughtorders',
    #                           on_delete=models.CASCADE, blank=True, default=None)

    class Meta:
        ordering = ('username',)
        verbose_name = 'buyer'

    def __str__(self):
        return self.username

