
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from . import models


def userCreate(request):
    newUser = models.User()
    newUser.username = request.username
    newUser.password = request.password
    return render(request, "user.html")
