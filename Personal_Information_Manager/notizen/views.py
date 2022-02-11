from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def userCreate(request):
    return render(request, "register.html")


def user(request):
    return render(request, "user.html")


def login(request):
    return render(request, "login.html", {})
