# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=40)
    translation = models.CharField(max_length=40)
    url_imagen = models.CharField(max_length=200, default='http://www.upforest.gov.in/Images/Default.png')
    pub_date = models.DateTimeField('date published')
    
    #Retorno lo url de la vista de detalle de la nueva palabra creada
    def get_absolute_url(self):
        return reverse('wordstore:index', kwargs={'word_id': self.pk})

    def __str__(self):
        return self.word