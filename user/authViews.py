import time

from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Buyer, userToken
from .serializers import BuyerSerializer, BuyerDetailSerializer
# Create your views here


class AuthView(APIView):
    """
    Login Method by username and password
    """
    def user_auth(self, username, password, retresult):
        try:
            instance = Buyer.objects.get(username=username, password=password)
            retresult['Status Code'] = status.HTTP_200_OK
            retresult['Found User'] = True
            retresult['Password Correct'] = True
            serializer = BuyerDetailSerializer(instance)
            retresult['User Data'] = serializer.data
            return retresult
        except Buyer.DoesNotExist:
            try:
                instance = Buyer.objects.get(username=username)
                if instance is not None:
                    retresult['Status Code'] = status.HTTP_404_NOT_FOUND
                    retresult['Found User'] = True
                    retresult['Password Correct'] = False
                    return retresult
            except Buyer.DoesNotExist:
                retresult['Status Code'] = status.HTTP_404_NOT_FOUND
                retresult['Found User'] = False
                retresult['Password Correct'] = False
                return retresult

    def post(self, request, *args, **kwargs):
        retresult = {
            'Status Code': None,
            'Found User': None,
            'Password Correct': None,
            'User Data': None
        }
        usr = request.data.get('username')
        pas = request.data.get('password')
        authResult = self.user_auth(usr, pas, retresult)
        return Response(authResult)
        # token = str(time.time()) + usr
        # print (token)
        # userToken.objects.update_or_create(username=usr, defaults={'token':token})
        # return Response(status=status.HTTP_200_OK)


