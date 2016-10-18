from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
import json


# Create your views here.

def home(request):
    print(request.session.keys())
    context = {
        "title" : "Portal do Conhecimento"
    }
    return render(request, "index.html", context)

def login(request):
    server_ip = settings.CMPAAS_CONF['server_address']
    server_port = settings.CMPAAS_CONF['server_port']
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    csrftoken = request.POST.get("csrfmiddlewaretoken", "")
    url = "http://"+server_ip+":"+server_port+"/o/token/"
    data = {'client_id':'KAivTIRh7e1ojpEGPh37rV5o3VDwDjeqjsIBMwE2',
            'client_secret':'mCZ27ZvCCK3lAQv06OpehN8WSwT8YWJAZ8I3XZmrxFygMh8qvPcMCNaK5YbiIP5GKntNIyKDU9cx0GXMH2arOjMLeGpdhMQaMvwxWti7t6nu8HKpcBg4pi8JxcbCQ2Iu',
            'grant_type':'password',
            'username':username,
            'password':password}
    headers = {'content-type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken}
    for key, value in requests.post(url, data=json.dumps(data), headers=headers).items():
        print(key, value)


    request.session['username'] = username

    context = {
        "title" : "Portal do Conhecimento",
        "username" : username
    }
    return render(request, "index.html", context)

def logout(request):

    # request for authentification

    request.session.clear()

    context = {
        "title" : "Portal do Conhecimento",
    }
    return render(request, "index.html", context)

def register(request):
    context = {
        "title" : "Portal do Conhecimento"
    }
    return render(request, "register.html", context)
