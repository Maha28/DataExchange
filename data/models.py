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


class Dom:
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
        
class EqualManager(models.Manager):
    def rule_8(self):
        for dom_element in Dom.get_elements():
            Equal(I=dom_element, J=dom_element)
            Equal.save()
    def rule_9(self):
        new_equal = list()
        for equal_element in Equal.objects.all():
            new_equal_element = Equal (I=equal_element.J, J=equal_element.I)
            new_equal.append(new_equal_element)   
        self.make_new_equal(new_equal) 
            
    def rule_10(self):
        new_equal = list()
        for equal_element in Equal.objects.all():
            if equal.element.J is equal_element.I:
                new_equal_element = Equal (I=equal_element.I, J=equal_element.J)
                new_equal.append(new_equal_element)   
        self.make_new_equal(new_equal) 
    
    def rule_11(self):
        new_equal = list()
        for mapping_element in Mapping.objects.all():
            new_equal_element = Equal (I=mapping_element.S, J=mapping_element.T)
            new_equal.append(new_equal_element) 
        self.make_new_equal(new_equal)      
    
    def rule_12(self):
        new_equal = list()
        for mapping_element in Mapping.objects.all():
            new_equal_element = Equal (I=mapping_element.T, J=mapping_element.S)
            new_equal.append(new_equal_element) 
        self.make_new_equal(new_equal)       
        
    def make_new_equal(self,new_equal):
        #Equal.objects.all().delete()
        for new_equal_element in new_equal:
            new_equal_element.save()
        
    def not_exausted(self):
        pass
        
    def generate_equal(self):
        while not_exausted():
            rule_8()
            rule_9()
            rule_10()
            rule_11()
        
    def get_equal(self):
        return Equal.objects.all()       
        
class Equal:
    objects = SourceManager()
    I = models.CharField(max_length=5)
    J = models.CharField(max_length=5)
    

          