# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Circunscripcion(models.Model):
	nombreCircunscripcion=models.CharField(max_length=200, default="Desconocida")
	numeroEscanhos=models.IntegerField(default=1)
	def __str__(self):
		return self.nombreCircunscripcion

class Mesa(models.Model):
	nombreMesa=models.CharField(max_length=200, default="Desconocida")
	id_nombreCircunscripcion=models.ForeignKey(Circunscripcion)
	def __str__(self):
		return self.nombreMesa
