from django.conf.urls import url
from django.conf import settings
from circunscripcion import views

urlpatterns = [
	url(r'^$', views.vistaCircunscripcion, name='vistaCircunscripcion'),
]
