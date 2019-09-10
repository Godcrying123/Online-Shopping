from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.request import Request

from .serializers import BuyerSerializer, AdminBuyerSerializer, BuyerDetailSerializer, UserSerializer
from .models import Buyer
from .permissions import IsOwnerReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BuyerList(generics.ListCreateAPIView):
    """
    General Method for Listing user instances
    """
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdminBuyerList(generics.ListCreateAPIView):
    """
    General Method for Listing user instances including all detailed user information
    """
    queryset = Buyer.objects.all()
    serializer_class = AdminBuyerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdminBuyerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a buyer instance for admin user
    """
    queryset = Buyer.objects.all()
    serializer_class = AdminBuyerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerReadOnly]


class BuyerDetailByName(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         generics.GenericAPIView):
    """
    Retrieve, or delete an buyer instance
    """
    serializer_class = BuyerDetailSerializer

    def get(self, request, username, *args, **kwargs):
        return self.retrieve(request, username, *args, **kwargs)

    def put(self, request, username, *args, **kwargs):
        return self.update(request, username, *args, **kwargs)

    def get_object(self, username):
        try:
            return Buyer.objects.get(username=username)
        except Buyer.DoesNotExist:
            raise Http404

    def retrieve(self, request, username, *args, **kwargs):
        instance = self.get_object(username)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, username, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object(username)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

