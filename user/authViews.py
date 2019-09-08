import time

from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Buyer, userToken
from .serializers import BuyerSerializer
# Create your views here


class AuthView(APIView):
    """
    Login Method by username and password
    """
    def get_object(self, username, password):
        try:
            return Buyer.objects.filter(username=username, password=password).first()
        except Buyer.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        usr = request.data.get('username')
        pas = request.data.get('password')
        buyer = self.get_object(usr, pas)
        serializer = BuyerSerializer(buyer)
        if buyer != None:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # token = str(time.time()) + usr
        # print (token)
        # userToken.objects.update_or_create(username=usr, defaults={'token':token})
        # return Response(status=status.HTTP_200_OK)



