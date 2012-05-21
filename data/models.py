from django.db import models

class Source1:
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)
    
class Source2:
    C = models.CharField(max_length=5)
    D = models.CharField(max_length=5)   
    
class Source2:
    E = models.CharField(max_length=5)
    F = models.CharField(max_length=5)       
    
class Mapping:
    S = models.CharField(max_length=5)
    T = models.CharField(max_length=5)      
    
class Target1:
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)      
    
class Target2:
    C = models.CharField(max_length=5)
    D = models.CharField(max_length=5)           