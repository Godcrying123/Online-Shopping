from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
# Create your models here.


class User(models.Model):
    name = models.CharField(_('name'), max_length=200, blank=True)
    # owner = models.ForeignKey('auth.User', related_name='person_entity', on_delete=models.CASCADE, blank=True)
    # isAdmin = models.BooleanField(default=False, verbose_name='IsAdmin')
    username = models.CharField(_('username'), max_length=200, db_index=True, unique=True)
    mail = models.EmailField(_('mail'), max_length=200, db_index=True)
    telephone = models.CharField(_('telephone'), max_length=100, blank=True)
    password = models.CharField(_('password'), max_length=200)
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

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

    def __str__(self):
        return self.username

    def owneduserinfos(self):
        return UserInfoEntity.objects.filter(Q(owner=self))


class UserInfoEntity(models.Model):
    owner = models.ForeignKey(User, verbose_name='Who Input', max_length=100,
                              related_name='own_user', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name='name', blank=True)
    recaddress = models.CharField(max_length=100, blank=True, verbose_name='receiver address')
    recaddresspostal = models.CharField(max_length=100, blank=True, verbose_name='receiver address postal')
    sendoutaddress = models.CharField(max_length=100, blank=True, verbose_name='deliver out address')
    sendoutaddresspostal = models.CharField(max_length=100, blank=True, verbose_name='deliver out address postal')
    mail = models.EmailField(max_length=200, db_index=True, verbose_name='E-mail')
    telephone = models.CharField(max_length=100, verbose_name='Telephone', blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='updated_time')

    class Meta:
        ordering = ('updated_time',)
        verbose_name = 'user informations'

    def __str__(self):
        return self.name


class UserToken(models.Model):
    username = models.OneToOneField(to='User', on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=100)

    class Meta:
        db_table = 'user_token'
        verbose_name = verbose_name_plural = 'user token table'

