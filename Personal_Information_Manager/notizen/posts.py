from django.http import HttpResponse
from django.core.exceptions import *
from django.shortcuts import redirect, render
from django.db import models
from .models import User, Lernobjekt
from .forms import FileFieldForm
import hashlib
import uuid


def userCreate(request):
    newUser = User()
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


def uploadFile(request):
    if request.method == 'POST':
        form = FileFieldForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = Lernobjekt(
                file=request.FILES['file'],
                user=User.objects.get(loghash=request.COOKIES['loghash']),
                name=request.POST['name'] or "",
                beschreibung=request.POST['beschreibung'] or "",
                kategorie=request.POST['kategorie'] or ""
            )
            instance.save()
            instance.refresh_from_db()
            return redirect('/account/')
    else:
        form = FileFieldForm()
    return render(request, 'upload.html', {'form': form})
