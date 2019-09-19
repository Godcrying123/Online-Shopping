from django.db import models
from product.models import Product
from user.models import Users
# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(Users, related_name='ownorders', verbose_name='order_owner',
                              on_delete=models.CASCADE, blank=False)
    STATUS_ORDER = (
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('cancel', 'Cancel'),
        ('delete', 'Delete'),
    )

    status_order = models.CharField(default='unpaid', max_length=10,
                                    choices=STATUS_ORDER, verbose_name='status_order', db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('-created',)

    # @classmethod
    # def create(cls, user):
    #     print(user)
    #     order = cls(owner=user)
    #     return order

    def __str__(self):
        return "Order {}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    STATUS_DELIVERY = (
        ('un-delivery', 'Un-Delivery'),
        ('in delivery', 'In-Delivery'),
        ('delivered', 'Delivered'),
    )
    order = models.ForeignKey(Order, verbose_name='belongsorder', related_name='orderitems', on_delete=models.CASCADE, blank=False)
    status_delivery = models.CharField(default='un-delivery', max_length=50, choices=STATUS_DELIVERY,
                                       verbose_name='status_delivery', db_index=True, blank=True)
    product = models.ForeignKey(Product, verbose_name='bought_products', related_name='boughtproducts',
                                on_delete=models.CASCADE, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        ordering = ('order',)

    def get_cost(self):
        return self.price * self.quantity
