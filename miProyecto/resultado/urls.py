from django.conf.urls import url
from django.conf import settings
from resultado import views

urlpatterns = [
	url(r'^$', views.vistaResultado, name='vistaResultado'),
]
