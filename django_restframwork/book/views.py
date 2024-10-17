from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets, authentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope

from book.serializers import BookSerializer, CategorySerializer
from book.models import Book, Category

class CategoryViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [IsAuthenticated]
   
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      elif self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()
   
class BookViewSet(viewsets.ModelViewSet):
   authentication_classes = [OAuth2Authentication]
   permission_classes = [IsAuthenticated]
   
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [IsAdminUser()]
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAuthenticated()]
      return super().get_permissions()