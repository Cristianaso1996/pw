from django.conf.urls import url
from django.conf import settings
from mesa.views import vistaMesa

urlpatterns = [
	url(r'^$', vistaMesa.as_view()),
]
