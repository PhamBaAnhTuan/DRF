from django.db import models
from django.utils import timezone

class Category(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=100)
   icon = models.TextField(null=True, blank=True)
   created_at = models.DateTimeField(default=timezone.now)
   updated_at = models.DateTimeField(auto_now=True)
   deleted_at = models.DateTimeField(null=True)
   
class Book(models.Model):
   id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=100)
   author = models.CharField(max_length=100)
   img = models.TextField(null=True, blank=True)
   price = models.IntegerField(default=0)
   discount = models.IntegerField(default=0)
   free_ship = models.BooleanField(default=False)
   description = models.TextField(null=True, blank=True)
   category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books', null=False)
   created_at = models.DateTimeField(default=timezone.now)
   updated_at = models.DateTimeField(auto_now=True)
   deleted_at = models.DateTimeField(null=True)

class Meta:
   ordering = ['-created_at']
   indexes = [
   models.Index(fields=['created_at'])
   ]