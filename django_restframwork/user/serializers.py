from .models import Customer
from django.contrib.auth.hashers import make_password, check_password, mask_hash
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = Customer
      fields = ('id', 'username', 'password')

   def create(self, validated_data):
      user = Customer(
         username=validated_data['username'],
         password=validated_data['password']
      )
      user.save()
      return user
   
   def validate_username(self, value):
      if Customer.objects.filter(username=value).exists():
         raise serializers.ValidationError("This username is already taken. Please choose another one.")
      return value