

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from app.forms import UserForm
from app.serializer import UserSerializer


# Create your views here.
@api_view(['POST', 'GET'])
def signUp(request):
    if request.method == 'GET':
        return render(request, "app/regist.html", {"form": UserForm})
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(access),
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)


@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'GET':
        return render(request, "app/login.html")
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)
        access = AccessToken.for_user(user)

        return Response({'refresh_token': str(refresh),
                         'access_token': str(access), }, status=status.HTTP_200_OK)
