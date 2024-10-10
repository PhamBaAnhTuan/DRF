from . import models
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
   class Meta:
      model = models.Book
      fields = '__all__'
      
class CategorySerializer(serializers.ModelSerializer):
   books = BookSerializer(many=True, read_only=True)
   class Meta:
      model = models.Category
      fields = '__all__'