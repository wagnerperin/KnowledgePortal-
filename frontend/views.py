from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests


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

    #request de autenticação

    context = {
        "title" : "Portal do Conhecimento",
        "username" : username
    }
    return render(request, "index.html", context)