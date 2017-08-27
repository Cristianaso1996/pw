# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from resultado.models import Resultado

# Create your views here.

def vistaResultado(request):
	listaResultados = Resultado.objects.all()
	context = {'listaResultados' : listaResultados}

	return render(request, "resultado.html", context)
