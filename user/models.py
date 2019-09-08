from django.db import models

from orders.models import Order
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    owner = models.ForeignKey('auth.User', related_name='person_entity', on_delete=models.CASCADE)
    username = models.CharField(max_length=200, db_index=True, unique=True, verbose_name='username')
    mail = models.EmailField(max_length=200, db_index=True, unique=True, verbose_name='E-mail')
    telephone = models.CharField(max_length=100, unique=True, verbose_name='Telephone')
    password = models.CharField(max_length=200, verbose_name='Password')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='updated_time')

    class Meta:
        ordering = ('username',)
        index_together = (('username', 'mail'),)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __int__(self, name, username, mail, telephone,  password, created_time):
        self.name = name
        self.username = username
        self.mail = mail
        self.telephone = telephone
        self.password = password
        self.created_time = created_time


class userToken(models.Model):
    username = models.OneToOneField(to='User', on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=100)

    class Meta:
        db_table = 'user_token'
        verbose_name = verbose_name_plural = 'user token table'


class Buyer(User):
    STATUS_VIP = (
        ('vip', 'VIP'),
        ('not-vip', 'Not VIP'),
    )
    STATUS_USER = (
        ('normal', 'Normal'),
        ('deleted', 'Deleted'),
        ('banned', 'Banned'),
    )
    status_vip = models.CharField(default='not-vip', max_length=10,
                                  choices=STATUS_VIP, verbose_name='status_vip', db_index=True)
    status_user = models.CharField(default='normal', max_length=10,
                                   choices=STATUS_USER, verbose_name='status_user', db_index=True)
    recaddress = models.CharField(max_length=100, blank=False)
    # orders = models.ForeignKey(Order, related_name='buyer_order', on_delete=models.CASCADE)

    class Meta:
        ordering = ('username',)
        verbose_name = 'buyer'

    def __str__(self):
        return self.username
