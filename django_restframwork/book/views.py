from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status, generics
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from book.serializers import BookSerializer, CategorySerializer
from book.models import Book, Category

class CategoryViewSet(viewsets.ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   permission_classes = [IsAuthenticated]
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      elif self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAdminUser()]
      return super().get_permissions()
   
class BookViewSet(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   permission_classes = [IsAuthenticated]
   
   def get_permissions(self):
      if self.action in ['list', 'retrieve']:
         return [AllowAny()]
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
         return [IsAdminUser()]
      return super().get_permissions()