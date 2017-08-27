from django import forms
from django.forms import ModelForm
from circunscripcion.models import Circunscripcion

class CircunscripcionForm(ModelForm):
	class Meta:
		model=Circunscripcion
		fields=['nombreCircunscripcion','numeroEscanhos']
