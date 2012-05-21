from django.db import models
import os
import random

class SourceManager(models.Manager):
    def populate_source(self):
        source = Source1(A=self.random_source_value(),B=self.random_source_value())
        source.save()
    
    def random_source_value(self):
        return os.urandom(1) +  random.randint(1,9)

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