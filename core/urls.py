from django.conf.urls import include
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('auth/', CustomAuthToken.as_view()),
    path('', include(router.urls)),
]
