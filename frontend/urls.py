from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
	url(r'^services/', views.services, name="services"),
    url(r'^editor/$', views.editor),
]
