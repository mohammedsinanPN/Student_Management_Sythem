from rest_framework import serializers
from .models import StudentDb
from django.contrib.auth.models import User


class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    class Meta:
        model=User
        fields= ['id','username','email','password']


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get('email'),
            password=validated_data.get("password")

        )
        return user



class StudentSerializer(serializers.ModelSerializer):   

    class Meta:
        model = StudentDb
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        read_only_fields = ["id","user","email","password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user