from django.shortcuts import render
import requests
import json
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
# Desabilitando o uso do HTTPS para testes locais
import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Create your views here.

api_url = 'http://127.0.0.1:8000'
client_id = '2DwBdhnIk9tznlqrVizAVn2SMGjzv7gyS6o9p7ys'
client_secret = 'ieHPfYtmhtvAqNSuchsJLW9eghBG9tQOexoE9LPmDUboLPDjTmNhiMCpR4nOjg84rMaHpSqa5PqThTms9W0r6A38zfiIHCiaGemU44Ykx0WDQUrzghsdCOBaV22x9mu0'
username = 'ramon'
password = '1234432q'

def home(request):
    oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
    token = oauth.fetch_token(token_url=api_url + '/o/token/',
        username=username, password=password, client_id=client_id,
        client_secret=client_secret)

    #data = json.loads(token)

    #request.session['username'] = username
    #request.session['access_token'] = ''
    #request.session['refresh_token'] = ''

    context = {
        'title': 'Portal do Conhecimento',
        'retorno': token
    }

    return render(request, 'knowledgeportal/index.html', context)

def register(request):
    context = {
        'title': 'Portal do Conhecimento - Registro'
    }
    return render(request, 'knowledgeportal/register.html', context)

def services(request):
    context = {
        'title': 'Portal do Conhecimento - Servicos'
    }
    return render(request, 'knowledgeportal/services.html', context)

def profile(request):
    context = {
        'title': 'Portal do Conhecimento - Profile'
    }
    return render(request, "knowledgeportal/profile.html", context)

def about(request):
    context = {
        'title': 'Portal do Conhecimento - Sobre'
    }
    return render(request, 'knowledgeportal/about.html', context)

def editor(request):
    context = {
        'title': 'Portal do Conhecimento - Editor de Mapas Conceituais'
    }

    return render(request, 'knowledgeportal/editor.html', context)