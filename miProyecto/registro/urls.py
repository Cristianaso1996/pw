from django.conf.urls import url
from django.conf import settings
from registro import views

urlpatterns = [
	url(r'^$', views.vistaRegistroIn, name='vistaRegistroIn'),
]
