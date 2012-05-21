from django.db import models

class Source1(models.Model):
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)
    
class Source2(models.Model):
    C = models.CharField(max_length=5)
    D = models.CharField(max_length=5)   
    
class Source2(models.Model):
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