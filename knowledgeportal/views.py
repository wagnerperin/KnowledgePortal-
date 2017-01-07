from django.shortcuts import render

# Create your views here.

def home(request):
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
    context = {
        'title': 'Portal do Conhecimento - Editor de Mapas Conceituais'
    }

    return render(request, 'knowledgeportal/editor.html', context)