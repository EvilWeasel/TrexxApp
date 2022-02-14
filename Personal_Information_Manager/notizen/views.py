from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def userCreate(request):
    return render(request, "register.html")


def user(request):
    return render(request, "user.html")


def userLogin(request):
    return render(request, "login.html")


def account(request):
    cookie = request.COOKIES.get('hash', 'none')
    if(cookie != 'none'):
        if(User.objects.filter(hash=cookie).exists()):
            user = User.objects.get(hash=cookie)
            return render(request, "account.html", user)
    return render(request, "login.html")
