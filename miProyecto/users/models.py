# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class EleccionUser(User):
  payment_details = models.TextField()
  postal_address = models.TextField()
    
  def __unicode__(self):
    return self.username + ": " + self.first_name + " " + self.last_name
