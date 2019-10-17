# from django.contrib.auth.models import User

from rest_framework import serializers

from user.models import User
from buyer.models import Buyer


class BuyerSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'password', 'mail', 'telephone']


class BuyerDetailSerializer(serializers.ModelSerializer):
    # RECEIVE_ADDRESS = (
    #     ('Primary Receive Address', None),
    # )
    # recaddress = serializers.MultipleChoiceField(choices=RECEIVE_ADDRESS, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'mail', 'telephone', 'password']


class AdminBuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        fields = ['id', 'name', 'username', 'mail', 'telephone', 'isAdmin', 'password', 'status_vip', 'status_user',
                  'recaddress', 'created_time', 'updated_time']
