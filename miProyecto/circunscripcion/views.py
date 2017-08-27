# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.contrib.auth.decorators import login_required, permission_required

from circunscripcion.models import Circunscripcion
from circunscripcion.forms import CircunscripcionForm

# Create your views here.

def vistaCircunscripcion(request):
	listaCircunscripciones = Circunscripcion.objects.all()
	context = {'listaCircunscripciones' : listaCircunscripciones}

	return render(request, "circunscripcion.html", context)

@login_required
@permission_required('circunscripcion.add_circunscripcion')
def addCircunscripcion(request):
	if request.method=='POST':
		form=CircunscripcionForm(request.POST)
		if form.is_valid():
			circunscripcion=form.save(commit=False)
			circunscripcion.save()
			return HttpResponseRedirect('/')

	else:
		form=CircunscripcionForm()

	context={'form':form}
	return render(request,'addCircunscripcion.html',context)

@login_required
@permission_required('circunscripcion.change_circunscripcion')
def changeCircunscripcion(request, pk):
	circunscripcion = get_object_or_404(Circunscripcion, pk=pk)
	if request.method=='POST':
		form=CircunscripcionForm(request.POST, instance=circunscripcion)
		if form.is_valid():
			circunscripcion=form.save(commit=False)
			circunscripcion.save()
			return redirect('/', pk=circunscripcion.pk)

	else:
		form=CircunscripcionForm(instance=circunscripcion)

	context={'form':form}
	return render(request,'changeCircunscripcion.html',context)

@login_required
@permission_required('circunscripcion.delete_circunscripcion')
def deleteCircunscripcion(request, pk):
	circunscripcion = get_object_or_404(Circunscripcion, pk=pk)
	if request.method=='POST':
		circunscripcion.delete()
		return redirect('/', pk=circunscripcion.pk)

	return render(request,'deleteCircunscripcion.html')
