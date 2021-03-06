# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import SignUpForm

# Create your views here.

def vistaRegistroIn(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect('/')
	else:
		form=SignUpForm()

	context={'form':form}
	return render(request,'registro.html',context)
