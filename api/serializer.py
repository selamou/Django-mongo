from rest_framework import serializers
from .models import Matiere, Cours,User,Td,Tp
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from .models import *
class filierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = ('__all__')
class ProfDserilizer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields= ['username','email','phone']
class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields =  ('__all__')
class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ('__all__')
class TdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Td
        fields = ('__all__')
class TpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tp
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','NNI')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'],validated_data['NNI'])

        return user
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class RegisterprofSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','phone')
        extra_kwargs = {'password': {'write_only': True}}

class loginprofSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    # def verify(self, validated_data):
    #     a = User.objects.get(username=validated_data['username'])
    #     user = ProfProfile.objects.get(user=a)
    #     return user

class RegisteruserSerializer(serializers.ModelSerializer):
    user = RegisterSerializer( )
    class Meta:
        model = EtudientProfile
        fields =( 'user', 'id_filiere')
        extra_kwargs = {'password': {'write_only': True}}

class loginuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class updateseriliser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'first_name','last_name')