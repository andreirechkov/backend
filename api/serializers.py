from django.db import transaction
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from chat.models import Chat
from .models import Test, Person


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'email', 'password']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['firstName', 'lastName', 'email', 'phone', 'typeUser']


class UserSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'person']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # Создание пользователей
    @transaction.atomic
    def create(self, validated_data):
        person_data = validated_data.pop('person')
        user = User.objects.create_user(**validated_data)
        user.person = Person.objects.create(user=user, **person_data)
        user.save()
        Token.objects.create(user=user)

        return user
