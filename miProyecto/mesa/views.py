# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.contrib.auth.decorators import login_required, permission_required

from mesa.models import Mesa, Circunscripcion
from mesa.forms import MesaForm

from django.views.generic import View

# Create your views here.

class vistaMesa(View):
	def get(self, request):
		listaMesas = Mesa.objects.all()
		context = {'listaMesas' : listaMesas}

		return render(request, "mesa.html", context)

class addMesa(View):
	form_class=MesaForm
	def get(self, request):
		form=self.form_class()
		context={'form':form}
		return render(request, 'addMesa.html', context)
	def post(self, request):
		form=self.form_class(request.POST)
		if form.is_valid():
			mesa=form.save(commit=False)
			mesa.save()
			return HttpResponseRedirect('/')

		context={'form':form}
		return render(request, 'addMesa.html', context)

class changeMesa(View):
	form_class=MesaForm
	def get(self, request, pk):		
		mesa = get_object_or_404(Mesa, pk=pk)
		form=self.form_class(instance=mesa)
		context={'form':form}
		return render(request,'changeMesa.html',context)
	def post(self, request, pk):
		mesa = get_object_or_404(Mesa, pk=pk)
		form=self.form_class(request.POST, instance=mesa)
		if form.is_valid():
			mesa=form.save(commit=False)
			mesa.save()
			return redirect('/', pk=mesa.pk)
			
		context={'form':form}
		return render(request,'changeMesa.html',context)
