from django.urls import path, include
from book.views import BookViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
   path('', include(router.urls)),
]
