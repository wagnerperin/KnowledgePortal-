from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^services/', views.services, name='services'),
    url(r'^editor/$', views.editor, name='editor'),
    url(r'^meusmapas/$', views.meusmapas, name='meusmapas'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^about/$', views.about, name='about'),
]