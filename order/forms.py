from django import forms
from user.models import UserInfoEntity
from django.db.models import Q
from .models import Order


class OrderCreateForm(forms.Form):
    name = forms.CharField(label='Receiver Name', max_length=100, required=True)
    email = forms.EmailField(label='Receiver E-mail', max_length=100, required=True)
    telephone = forms.CharField(label='Receiver Telephone', max_length=100, required=True)
    postal = forms.CharField(label='Receiver Address Postal', max_length=100, required=False)
    address = forms.CharField(label='Receiver Address', max_length=100, required=True)

    # AVAILABLE_USER_INFO_ENTITY = None
    #
    # def __init__(self, *args, **kwargs):
    #     self.owner = kwargs.pop('owner', None)
    #     # self.AVAILABLE_USER_INFO_ENTITY = [(user) for user in self.owner.owneduserinfos]
    #     self.AVAILABLE_USER_INFO_ENTITY = UserInfoEntity.objects.filter(Q(owner=self.owner))
    #     print(self.AVAILABLE_USER_INFO_ENTITY)
    #     # self.receiver.choices = self.AVAILABLE_USER_INFO_ENTITY
    #     super().__init__(*args, **kwargs)