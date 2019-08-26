from django.db import models
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    username = models.CharField(max_length=200, db_index=True, unique=True, verbose_name='username')
    mail = models.EmailField(max_length=200,db_index=True, unique=True, verbose_name='E-mail')
    password = models.CharField(max_length=200, verbose_name='Password')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='created_time')

    class Meta:
        ordering = ('username',)
        index_together = (('username', 'mail'),)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __int__(self, name, username, mail, password, created_time):
        self.name = name
        self.username = username
        self.mail = mail
        self.password = password
        self.created_time = created_time
