from django.db import models

# Create your models here.


class Store(models.Model):
    STATUS_ITEMS = (
        ('normal', 'Normal'),
        ('deleted', 'Deleted'),
        ('banned', 'Banned'),
        ('popular', 'Popular'),
    )
    status = models.CharField(default='normal', max_length=10,
                              choices=STATUS_ITEMS, verbose_name='store_status', db_index=True )
    store_name = models.CharField(max_length=200, db_index=True, unique=True, verbose_name='store name')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')
    store_location = models.CharField(max_length=200, db_index=True, verbose_name='store location')
    store_fans = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('store_name',)
        verbose_name = 'store'
        verbose_name_plural = 'stores'

    def __str__(self):
        return self.store_name
