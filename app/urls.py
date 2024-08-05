from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify
from .views import KakaoLogin, NaverLogin

from app import views

urlpatterns = [
    path('register/', views.signUp),
    path('login/', views.login),
    path('api/token/', token_obtain_pair),
    path('api/token/refresh/', token_refresh),
    path('api/token/verify/', token_verify),
    path('dj-rest-auth/kakao/finish/', KakaoLogin.as_view(), name='kakao_login'),
    path('dj-rest-auth/naver/finish/', NaverLogin.as_view(), name='naver_login'),
]