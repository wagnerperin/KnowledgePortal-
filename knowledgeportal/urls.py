from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout$', views.logout),
    url(r'^services/', views.services, name="services"),
    url(r'^editor/$', views.editor),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^about/$', views.about, name='about'),
]