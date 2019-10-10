from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import Buyer, User
from user.api.serializers import BuyerSerializer


# Create your views here


class AuthView(APIView):
    """
    Login Method by username and password
    """
    def user_auth(self, username, password, retresult):
        try:
            instance = User.objects.get(username=username, password=password)
            retresult['Status_Code'] = status.HTTP_200_OK
            retresult['User_Verified'] = True
            serializer = BuyerSerializer(instance)
            retresult['User Data'] = serializer.data
            return retresult
        except User.DoesNotExist:
            retresult['Status_Code'] = status.HTTP_404_NOT_FOUND
            retresult['User_Verified'] = False
            return retresult

    def post(self, request, *args, **kwargs):
        retresult = {
            'Status_Code': None,
            'User_Verified': None,
            'User_Data': None
        }
        usr = request.data.get('username')
        pas = request.data.get('password')
        authResult = self.user_auth(usr, pas, retresult)
        return Response(authResult)
        # token = str(time.time()) + usr
        # print (token)
        # userToken.objects.update_or_create(username=usr, defaults={'token':token})
        # return Response(status=status.HTTP_200_OK)



