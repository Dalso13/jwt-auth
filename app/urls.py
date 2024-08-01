from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify

from app import views

urlpatterns = [
    path('register/', views.signUp),
    path('login/', views.login),
    path('api/token/', token_obtain_pair),
    path('api/token/refresh/', token_refresh),
    path('api/token/verify', token_verify),
]