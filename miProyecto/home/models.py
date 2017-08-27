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

class Partido(models.Model):
	nombrePartido=models.CharField(max_length=200, default="Desconocido")
	id_nombreCircunscripcion=models.ForeignKey(Circunscripcion)
	def __str__(self):
		return self.nombrePartido

class Resultado(models.Model):
	resultado=models.IntegerField()
	def __str__(self):
		return self.resultado

class Resultado_Partido(models.Model):
	id_partido=models.ForeignKey(Partido)
	id_resultado=models.ForeignKey(Resultado)
	votos=models.IntegerField(default=0)
	def __str__(self):
		return self.votos

class Resultado_Mesa(models.Model):
	id_mesa=models.ForeignKey(Mesa)
	id_resultadoM=models.ForeignKey(Resultado)
	def __unicode__(self):
		return self.id_mesa+"_"+self.id_resultadoM
