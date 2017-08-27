from django import forms
from django.forms import ModelForm
from mesa.models import Mesa

class MesaForm(ModelForm):
	class Meta:
		model=Mesa
		fields=['nombreMesa','id_nombreCircunscripcion']
