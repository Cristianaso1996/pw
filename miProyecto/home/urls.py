from django.conf.urls import url
from django.conf import settings
from home import views

urlpatterns = [
	url(r'^$', views.vistaHome, name='vistaHome'),
]
