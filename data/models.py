import os, random, string
from django.db import models

class SourceManager(models.Manager):
    def populate_source(self):
        source = Source1(A=id_generator(2),B=id_generator(2))
        source.save()

class Source1(models.Model):    
    objects = SourceManager()
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)
    
class Source2(models.Model):
    objects = SourceManager()
    C = models.CharField(max_length=5)
    D = models.CharField(max_length=5)   
    
class Source2(models.Model):
    objects = SourceManager()
    E = models.CharField(max_length=5)
    F = models.CharField(max_length=5)       
    
class Mapping(models.Model):
    S = models.CharField(max_length=5)
    T = models.CharField(max_length=5)      
    
class Target1(models.Model):
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)      
    
class Target2(models.Model):
    C = models.CharField(max_length=5)
    D = models.CharField(max_length=5)     
    
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):  
    return ''.join(random.choice(chars) for x in range(size)) 
          