import os, random, string
from django.db import models

class SourceManager(models.Manager):
    MAX_RANDOM_ENTRIES = 10
    
    def populate_source(self):
        i = 0
        while i<self.MAX_RANDOM_ENTRIES:
            source1 = Source1(A=source_generator(2),B=source_generator(2))
            source2 = Source2(A=source_generator(2),B=source_generator(2))
            source3 = Source3(A=source_generator(2),B=source_generator(2))
            source1.save()
            source2.save()
            source3.save()
            i = i+1
    
    def get_source1(self):
        return Source1.objects.all() 
      
    def get_source2(self):
        return Source2.objects.all() 
    
    def get_source3(self):
        return Source3.objects.all()         
    
    def clear_source(self):
        Source1.objects.all().delete()
        Source2.objects.all().delete() 
        Source3.objects.all().delete()  

class Source1(models.Model):    
    objects = SourceManager()
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)
    
class Source2(models.Model):
    objects = SourceManager()
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)   
    
class Source3(models.Model):
    objects = SourceManager()
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)       

class MappingManager(models.Manager):
    MAX_RANDOM_ENTRIES = 10
    
    def populate_mapping(self):
        i = 0
        while i<self.MAX_RANDOM_ENTRIES:
            mapping = Mapping(S=source_generator(2),T=target_generator(2))
            mapping.save()
            i = i+1
    
    def get_mapping(self):
        return Mapping.objects.all()   
    
    def clear_mapping(self):
        Mapping.objects.all().delete()

class Mapping(models.Model):
    objects = MappingManager()
    S = models.CharField(max_length=5)
    T = models.CharField(max_length=5)      
    
class Target1(models.Model):
    X = models.CharField(max_length=5)
    Y = models.CharField(max_length=5)      
    
class Target2(models.Model):
    X = models.CharField(max_length=5)
    Y = models.CharField(max_length=5)     
    
def source_generator(size=6, chars=string.ascii_uppercase + string.digits):  
    return ''.join(random.choice(chars) for x in range(size)) 

def target_generator(size=6, chars=string.digits):  
    return '_'.join(random.choice(chars) for x in range(size)) 


class DOM:
    dom_elements = list()
    
    def generate(self, source, mapping):
        for source_element in source.objects.all():
            self.dom_elements.append(source_element.A)
            self.dom_elements.append(source_element.B)
        for mapping_element in mapping.objects.all():
            self.dom_elements.append(mapping_element.S)
            self.dom_elements.append(mapping_element.T)
        #Remove duplicates    
        self.dom_elements = list(set(self.dom_elements))    
        
    def get_elements(self):
        return self.dom_elements
        
class EQUAL:
    pass
          