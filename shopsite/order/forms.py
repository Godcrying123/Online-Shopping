from django import forms
from django.utils.translation import gettext_lazy as _
from user.models import UserInfoEntity
from django.db.models import Q
from .models import Order


class OrderCreateForm(forms.Form):
    name = forms.CharField(label=_('Receiver Name'), max_length=100, required=True)
    email = forms.EmailField(label=_('Receiver Email'), max_length=100, required=True)
    telephone = forms.CharField(label=_('Receiver Telephone'), max_length=100, required=True)
    postal = forms.CharField(label=_('Receiver Address Postal'), max_length=100, required=False)
    address = forms.CharField(label=_('Receiver Address'), max_length=100, required=True)

    # AVAILABLE_USER_INFO_ENTITY = None
    #
    # def __init__(self, *args, **kwargs):
    #     self.owner = kwargs.pop('owner', None)
    #     # self.AVAILABLE_USER_INFO_ENTITY = [(user) for user in self.owner.owneduserinfos]
    #     self.AVAILABLE_USER_INFO_ENTITY = UserInfoEntity.objects.filter(Q(owner=self.owner))
    #     print(self.AVAILABLE_USER_INFO_ENTITY)
    #     # self.receiver.choices = self.AVAILABLE_USER_INFO_ENTITY
    #     super().__init__(*args, **kwargs)