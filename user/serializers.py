from django.contrib.auth.models import User

from rest_framework import serializers

from .models import User, Buyer


class UserSerializer(serializers.ModelSerializer):
    buyer = serializers.PrimaryKeyRelatedField(many=True, queryset=Buyer.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'buyer']


class BuyerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Buyer
        fields = ['id', 'owner', 'name', 'username', 'password']


class BuyerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        fields = ['id', 'name', 'username', 'mail', 'telephone', 'password', 'recaddress']


class AdminBuyerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Buyer
        fields = ['id', 'owner', 'name', 'username', 'mail', 'telephone', 'password', 'status_vip', 'status_user',
                  'recaddress', 'created_time', 'updated_time']
