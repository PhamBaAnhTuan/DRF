from django.db import models
from django.contrib.auth.models import User
import datetime

from book.models import Book

class Customer(models.Model):
   id = models.AutoField(primary_key=True)
   firstName = models.CharField(max_length=128, blank=True)
   lastName = models.CharField(max_length=128, blank=True)
   phone = models.CharField(max_length=15, blank=True)
   email = models.EmailField(max_length=100)
   username = models.CharField(max_length=100)
   password = models.CharField(max_length=100)
   
   def __str__(self):
      return f'{self.id} {self.firstName} {self.lastName}'
     
class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   date_modified = models.DateTimeField(User, auto_now=True)
   phone = models.CharField(max_length=15, blank=True)
   address  = models.CharField(max_length=200, blank=True)
   old_cart = models.CharField(max_length=200, blank=True, null=True)

   def __str__(self):
      return self.user.username
   
class Order(models.Model):
   book = models.ForeignKey(Book, on_delete=models.CASCADE)
   customer = models.ForeignKey(Customer, on_delete=models.CASCADE),
   quantity = models.IntegerField(default = 1)
   address = models.CharField(max_length=150, default='', blank=True)
   phone = models.CharField(max_length=20, default='', blank=True)
   date = models.DateField(default=datetime.datetime.today)
   status = models.BooleanField(default=False)

   def __str__(self):
      return self.book