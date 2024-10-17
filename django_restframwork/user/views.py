from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

from rest_framework import status, viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from oauth2_provider.views import TokenView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Customer, User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]

   @action(methods=['POST'], detail=False, url_path='signup', permission_classes=[AllowAny])
   def signUp(self, request):
      serializer = UserSerializer(data=request.data)

      if serializer.is_valid():
         user = serializer.save()
         print(f'Signed up: {request.data.get("username")}')
         return Response({"message": "Signup successfully!"}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   @action(methods=['POST'], detail=False, url_path='signin', permission_classes=[AllowAny])
   def signIn(self, request):
      username = request.data.get('username')
      password = request.data.get('password')

      if username and password:
         user = authenticate(request, username=username, password=password)
         
         if user is not None:
            token_request_data = {
               'grant_type': 'password',
               'username': username,
               'password': password,
               'client_id': 'mXFmoA3VwA5JsZxmFjzNZWD4L6aK8cUHoy090eJl',
               'client_secret': 'oauth2'
            }
            response = TokenView(data=token_request_data)
            return Response({"message": "Sign in successfully!", "token": response.data}, status=status.HTTP_200_OK)
         else:
               return Response({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
      else:
         return Response({"error": "Username and password required!"}, status=status.HTTP_400_BAD_REQUEST)