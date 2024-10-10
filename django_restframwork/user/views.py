from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

from rest_framework import status, viewsets, serializers
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import Customer, User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = Customer.objects.all()
   serializer_class = UserSerializer
   @action(methods=['POST'], detail=False, url_path='signup')
   def signUp(self, request):
      serializer = UserSerializer(data=request.data)

      if serializer.is_valid():
         user = serializer.save()
         print(f'Signed up: {request.data.get("username")}')
         return Response({"message": "Signup successfully!"}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   @action(methods=['POST'], detail=False, url_path='signin')
   def signIn(self, request):
      username = request.data.get('username')
      password = request.data.get('password')

      if username and password:
         user = authenticate(request, username=username, password=password)

         if user is not None:
               token = AccessToken.for_user(user)
               login(request, user)    # create a new session
               print(f'Signed in: {username}')
               return Response({"message": "Sign in successfully!", "token": str(token)}, status=status.HTTP_200_OK)
         else:
               return Response({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
      else:
         return Response({"error": "Username and password required!"}, status=status.HTTP_400_BAD_REQUEST)