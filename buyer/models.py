from django.db import models
from user.models import User
# Create your models here.


class Buyer(User):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_BANNED = 2
    STATUS_ISVIP = 3
    STATUS_ITEMS = (
        {STATUS_NORMAL, 'normal'},
        {STATUS_DELETE, 'deleted'},
        {STATUS_BANNED, 'banned'},
        {STATUS_ISVIP, 'vip user'},
    )

    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='buyer status')

