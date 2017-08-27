"""miProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))		
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from django.contrib.auth.decorators import permission_required

from circunscripcion import views as viewsC
from mesa.views import addMesa, changeMesa

urlpatterns = [
		url(r'^admin/', admin.site.urls),
		url(r'^', include('home.urls')),
		url(r'^home/circunscripciones/', include('circunscripcion.urls')),
		url(r'^home/mesas/', include('mesa.urls')),
		url(r'^home/resultados/', include('resultado.urls')),
		url(r'^home/registro/', include('registro.urls')),
		url(r'^home/login/', login, {'template_name': 'login.html', }, name='login'),
		url(r'^accounts/profile/', include('home.urls')),
		url(r'^accounts/profile/home/circunscripciones/', include('circunscripcion.urls')),
		url(r'^accounts/profile/home/circunscripciones/addCircunscripcion/', viewsC.addCircunscripcion, name='addCircunscripcion'),	
		url(r'^home/circunscripciones/addCircunscripcion/', viewsC.addCircunscripcion, name='addCircunscripcion'),
		url(r'^accounts/profile/home/circunscripciones/(?P<pk>[-\w]+)/changeCircunscripcion', viewsC.changeCircunscripcion, name='changeCircunscripcion'),	
		url(r'^home/circunscripciones/(?P<pk>[-\w]+)/changeCircunscripcion', viewsC.changeCircunscripcion, name='changeCircunscripcion'),
		url(r'^accounts/profile/home/circunscripciones/(?P<pk>[-\w]+)/deleteCircunscripcion', viewsC.deleteCircunscripcion, name='deleteCircunscripcion'),	
		url(r'^home/circunscripciones/(?P<pk>[-\w]+)/deleteCircunscripcion', viewsC.deleteCircunscripcion, name='deleteCircunscripcion'),
		url(r'^accounts/profile/home/mesas/', include('mesa.urls')),
		url(r'^accounts/profile/home/mesas/addMesa/', addMesa.as_view()),
		url(r'^home/mesas/addMesa/', addMesa.as_view()),
		url(r'^accounts/profile/home/mesas/(?P<pk>[-\w]+)/changeMesa', changeMesa.as_view()),	
		url(r'^home/mesas/(?P<pk>[-\w]+)/changeMesa', changeMesa.as_view()),
		url(r'^accounts/profile/home/logout/', logout, {'template_name': 'logout.html', }, name='logout'),
		url(r'^home/logout/', logout, {'template_name': 'logout.html', }, name='logout'),
]
