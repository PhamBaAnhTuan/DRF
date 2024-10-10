from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status, generics
from rest_framework.decorators import action

from django.contrib.auth.hashers import make_password
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from book.serializers import BookSerializer, CategorySerializer
from book.models import Book, Category
   
class CategoryViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
   permission_classes = [AllowAny]
   
   queryset = Category.objects.all()
   serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
   # permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
   permission_classes = [AllowAny]
     
   queryset = Book.objects.all()
   serializer_class = BookSerializer