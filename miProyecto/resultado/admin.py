# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib import admin
from resultado.models import Circunscripcion, Mesa, Partido, Resultado, Resultado_Partido, Resultado_Mesa

# Register your models here.

admin.site.register(Circunscripcion)
admin.site.register(Mesa)
admin.site.register(Partido)
admin.site.register(Resultado)
admin.site.register(Resultado_Partido)
admin.site.register(Resultado_Mesa)
