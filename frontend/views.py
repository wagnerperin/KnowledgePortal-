from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import requests
import json


# Create your views here.

def home(request):
    print(request.session.keys())
    context = {
        "title": "Portal do Conhecimento"
    }
    return render(request, "index.html", context)


def login(request):
    server_ip = settings.CMPAAS_CONF['server_address']
    server_port = settings.CMPAAS_CONF['server_port']
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    access_token = request.POST.get("access_token", "")
    token_type = request.POST.get("token_type", "")
    expires_in = request.POST.get("expires_in", "")
    refresh_token = request.POST.get("refresh_token", "")
    scope = request.POST.get("scope", "")

    request.session['username'] = username
    request.session['access_token'] = access_token
    request.session['expires_in'] = expires_in
    request.session['refresh_token'] = refresh_token
    request.session['scope'] = scope

    context = {
        "title": "Portal do Conhecimento",
    }
    return redirect("/", context)


def logout(request):

    # request for authentification

    request.session.clear()

    context = {
        "title": "Portal do Conhecimento",
    }
    # return render(request, "index.html", context
    return redirect("/", context)


# def logout(request):
#
#     # request for authentification
#
#     request.session.clear()
#
#     context = {
#         "title" : "Portal do Conhecimento",
#     }
#     return render(request, "index.html", context)

def register(request):
    context = {
        "title": "Portal do Conhecimento"
    }
    return render(request, "register.html", context)

def services(request):
    context = {
        "title": "Portal do Conhecimento"
    }
    return render(request, "services.html", context)
