from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import mixins

from .serializers import BuyerSerializer, AdminBuyerSerializer, BuyerDetailSerializer
from .models import Buyer
from .permissions import IsOwnerReadOnly

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class BuyerList(generics.CreateAPIView):
    """
    the api for user registrations
    """
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class AdminBuyerList(generics.ListAPIView):
    """
    General Method for Listing user instances including all detailed user information
    """
    queryset = Buyer.objects.all()
    serializer_class = AdminBuyerSerializer


class AdminBuyerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a buyer instance for admin user
    """
    queryset = Buyer.objects.all()
    serializer_class = AdminBuyerSerializer


class BuyerDetailByName(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    """
    user profile details and update
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

    def perform_update(self, serializer):
        serializer.save()


