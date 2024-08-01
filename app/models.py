from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from app.managers import UserManager


# Register your models here.


# AbstractBaseUser를 상속해서 유저 커스텀
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'

# Create your models here.
# class User(AbstractUser):
#     phone = models.CharField(max_length=20)
