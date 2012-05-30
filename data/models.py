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
    

class Dom(models.Model):
    dom = list()
    
    def generate_dom(self, source, mapping):
        for source_element in source.objects.all():
            self.dom.append(source_element.A)
            self.dom.append(source_element.B)
        for mapping_element in mapping.objects.all():
            self.dom.append(mapping_element.S)
            self.dom.append(mapping_element.T)
        #Remove duplicates    
        self.dom = list(set(self.dom))    
        
    def get_dom(self):
        return self.dom
        
class EqualManager(models.Manager):
    dom = models.OneToOneField(Dom,primary_key=True) 
    
    def get_dom(self):
        return self.dom.get_dom()
    
    def rule_8(self):
        self.dom.generate_dom()
        for dom in self.get_dom():
            new_equal = Equal(I=dom, J=dom)
            new_equal.save()
            
    def rule_9(self):
        for equal_element in Equal.objects.all():
            new_equal = Equal (I=equal_element.J, J=equal_element.I)
            new_equal.save()  
            
    def rule_10(self):
        for equal_element in Equal.objects.all():
            if equal.element.J is equal_element.I:
                new_equal = Equal (I=equal_element.I, J=equal_element.J)
                new_equal.save()       
    
    def rule_11(self):
        for mapping_element in Mapping.objects.all():
            new_equal = Equal (I=mapping_element.S, J=mapping_element.T)
            new_equal.save()   
    
    def rule_12(self):
        for mapping_element in Mapping.objects.all():
            new_equal = Equal (I=mapping_element.T, J=mapping_element.S)
            new_equal.save()  
        
    def not_exausted(self):
        return False
        
    def generate_equal(self):
        self.rule_8()
        self.rule_9()
        self.rule_10()
        self.rule_11()
      
    def clear_equal(self):
        Equal.objects.all().delete()       
        
class Equal(models.Model):
    objects = EqualManager()
    I = models.CharField(max_length=5)
    J = models.CharField(max_length=5)
    
        
#Helpers        
def source_generator(size=6, chars=string.ascii_uppercase + string.digits):  
    return ''.join(random.choice(chars) for x in range(size)) 

def target_generator(size=6, chars=string.digits):  
    return '_'.join(random.choice(chars) for x in range(size)) 

          