from django.http import Http404
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import BuyerSerializer, UserSerializer
from .models import Buyer
from .permissions import IsOwnerReadOnly


class BuyerList(generics.ListCreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BuyerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerReadOnly]


class BuyerDetailByName(APIView):
    """
    Retrieve, update or delete a buyer instance
    """

    def get_object(self, username):
        try:
            return Buyer.objects.get(username=username)
        except Buyer.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        buyer = self.get_object(username)
        serializer = BuyerSerializer(buyer)
        return Response(serializer.data)

    def put(self, request, username, format=None):
        buyer = self.get_object(username)
        serializer = BuyerSerializer(buyer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        buyer = self.get_object(username)
        buyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
