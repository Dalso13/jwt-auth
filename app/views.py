from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from app.forms import UserForm
from app.models import User

# Create your views here.
register = CreateView.as_view(
    template_name='app/regist.html',
    model=User,
    form_class=UserForm,
    success_url="/",
)
