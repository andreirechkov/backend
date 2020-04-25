from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import TestSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Test


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        responce = super(GetAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=responce.data['token'])
        user = User.objects.get(id=token.user_id)
        userSerializer = UserSerializer(user, many=False)

        return Response({'token': token.key, 'id': token.user_id})
