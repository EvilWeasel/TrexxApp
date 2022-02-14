from django.http import HttpResponse
from django.core.exceptions import *
from django.shortcuts import redirect, render
from django.db import models
from . import models
import hashlib
import uuid


def userCreate(request):
    newUser = models.User()
    newUser.username = request.POST['firstname']
    newUser.email = request.POST['email']
    newUser.password = request.POST['password']
    # speichert user in db
    newUser.save()
    # save cookie with user id

    return render(request, 'user.html', {'newUser': newUser})


def userLogin(request):
    loginEmail = request.POST['email']
    loginPassword = request.POST['password']
    salt = uuid.uuid4().hex
    loginHash = hashlib.sha256(
        salt.encode() + loginPassword.encode()).hexdigest()
    try:
        loginUser = models.User.objects.filter(
            email=loginEmail, password=loginPassword).get()
    except ObjectDoesNotExist:
        print('User with this password does not exist')
        render(request, 'login.html')
    loginUser.loghash = loginHash
    loginUser.save()
    loginUser.refresh_from_db()
    Result = redirect('/account/', loginUser)
    Result.set_cookie('loghash', loginUser.loghash,
                      max_age=60 * 60 * 24 * 1)
    return Result
