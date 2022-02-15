from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import User, Lernobjekt
from .forms import FileFieldForm


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
    cookie = request.COOKIES['loghash']
    if(cookie != 'none'):
        if(User.objects.filter(loghash=cookie).exists()):
            user = User.objects.get(loghash=cookie)
            return render(request, "account.html", {'user': user})
    return redirect(request, "login.html")


def userUpload(request):
    return render(request, "account_file.html")


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
