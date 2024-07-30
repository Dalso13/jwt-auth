from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import token_verify, token_refresh, token_obtain_pair

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.signUp),
    path('login/', views.login),
    path('api/token/', token_obtain_pair),
    path('api/token/refresh/', token_refresh),
    path('api/token/verify', token_verify),
]
