from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password, mask_hash
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = (
         'id', 
         'is_superuser',
         'username',
         'password',
         'first_name',
         'last_name',
      )
      # fields = '__all__'

   def create(self, validated_data):
      user = User(
         username=validated_data['username'],
         password=validated_data['password']
      )
      user.set_password(validated_data['password'])
      user.save()
      return user