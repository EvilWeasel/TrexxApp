from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def userCreate(request):
<<<<<<< Updated upstream
    return render(request, "register.html")
=======
    return render(request, "userCreate.html")
>>>>>>> Stashed changes


def user(request):
    return render(request, "user.html")
