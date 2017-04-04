from django.shortcuts import render, redirect
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

def verifica_login(request):
    if request.session.get('access_token'):
        return True
    else:
        return False

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not verifica_login(request):
            oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))

            try:
                token = oauth.fetch_token(token_url=api_url + '/o/token/',
                    username=username, password=password, client_id=client_id,
                    client_secret=client_secret)
            except:
                context = {
                    'title': 'Portal do Conhecimento',
                    'erro': 'Nao foi possivel realizar o login. Tente novamente.'
                }
                
                return render(request, 'knowledgeportal/index.html', context)


            data = json.loads(json.dumps(token))

            request.session['username'] = username
            request.session['access_token'] = data['access_token']
            request.session['refresh_token'] = data['refresh_token']
    
    return redirect('/')

def logout(request):
    try:
        del request.session['username']
        del request.session['access_token']
        del request.session['refresh_token']
    except KeyError:
        pass
    return redirect('/')

def home(request):
    #login(request)

    context = {
        'title': 'Portal do Conhecimento'
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

    url = api_url + '/api/maps/'
    headers = {'Authorization': 'Bearer ' + request.session.get('access_token'), 'Content-Type': 'application/json'}

    if request.method == 'POST':
        titulo_mapa = request.POST['titulo_mapa']
        question = request.POST['question']
        description = request.POST['titulo_mapa']

        payload = {'title': titulo_mapa, 'question': question, 'description': description}

        r = requests.post(url, headers=headers, data=json.dumps(payload))

    r = requests.get(url, headers=headers)

    context = {
        'title': 'Portal do Conhecimento - Editor de Mapas Conceituais',
        'mapas': json.loads(r.text)
    }

    return render(request, 'knowledgeportal/editor.html', context)