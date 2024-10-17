from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.UserViewSet, basename='user')

urlpatterns = [
   path('', include(router.urls)),
   # path('signin/', views.signIn, name='signin'),
   # path('token/', views.CustomTokenView.as_view(), name='token'),
]