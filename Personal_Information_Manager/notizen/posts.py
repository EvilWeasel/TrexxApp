
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from . import models


def userCreate(request):
    newUser = models.User()
    newUser.username = request.POST["firstname"]
    newUser.email = request.POST['email']
    newUser.password = request.POST['password']
    # speichert user in db
    newUser.save()
    # save cookie with user id

    return render(request, "user.html", {"newUser" : newUser})
