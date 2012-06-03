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
    A = models.CharField(max_length=5,primary_key=True)
    B = models.CharField(max_length=5,primary_key=True)
    
class Source2(models.Model):
    objects = SourceManager()
    A = models.CharField(max_length=5,primary_key=True)
    B = models.CharField(max_length=5,primary_key=True)   
    
class Source3(models.Model):
    objects = SourceManager()
    A = models.CharField(max_length=5,primary_key=True)
    B = models.CharField(max_length=5,primary_key=True)       

class MappingManager(models.Manager):
    MAX_RANDOM_SOURCE = 10
    MAX_RANDOM_TARGET = 5    
    def populate_mapping(self):
        S = []
        T = []
        for i in range(0,self.MAX_RANDOM_SOURCE):
            S.append(source_generator(2))
            T.append(target_generator(2)) 
            if i < self.MAX_RANDOM_TARGET: T.append(target_generator(2)) 
            else: T.append(S[i])
            mapping = Mapping(S=S[i],T=T[i])
            mapping.save()
    
    def clear_mapping(self):
        Mapping.objects.all().delete()

class Mapping(models.Model):
    objects = MappingManager()
    S = models.CharField(max_length=5,primary_key=True)
    T = models.CharField(max_length=5,primary_key=True)      
    
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
    
    def clear_dom(self):
        self.dom = list()
        
class EqualManager(models.Manager):
    dom = Dom() 
    current_objects_count = -1
    
    def get_dom(self):
        return self.dom.get_dom()
    
    def rule_8(self):
        for dom in self.get_dom():
            new_equal = Equal(I=dom, J=dom)
            new_equal.save()
            
    def rule_9(self):
        for equal_element in Equal.objects.all():
            new_equal = Equal (I=equal_element.J, J=equal_element.I)
            new_equal.save()       
                
    def rule_10(self):
        for equal_element1 in Equal.objects.all():            
            for equal_element2 in Equal.objects.all():            
                if equal_element1.J is equal_element2.I:                
                    new_equal = Equal (I=equal_element1.I, J=equal_element2.J)                
                    new_equal.save()                  
             
    def rule_11(self):
        for mapping_element1 in Mapping.objects.all():            
            for mapping_element2 in Mapping.objects.all():
                if mapping_element1.T is mapping_element2.T:          
                    new_equal = Equal (I=mapping_element1.S, J=mapping_element2.S)            
                    new_equal.save()        
            
    def rule_12(self):
        for mapping_element1 in Mapping.objects.all():            
            for mapping_element2 in Mapping.objects.all(): 
                if mapping_element1.S is mapping_element2.S:  
                    new_equal = Equal (I=mapping_element1.T, J=mapping_element2.T)            
                    new_equal.save()                  
        
    def not_exausted(self, new_objects_count):
        if self.current_objects_count is new_objects_count:
            return False
        else:
            self.current_objects_count = new_objects_count
            return True
        
    def generate_equal(self,source, mapping):
        while self.not_exausted(Equal.objects.all().count()):
            self.dom.generate_dom(source, mapping)
            self.rule_8()
            self.rule_9()
            self.rule_10()
            self.rule_11()
            self.rule_12()
            
    def clear_equal(self):
        Equal.objects.all().delete() 
        self.dom.clear_dom()     
        
class Equal(models.Model):
    objects = EqualManager()
    I = models.CharField(max_length=5, primary_key=True)
    J = models.CharField(max_length=5, primary_key=True)
    
        
#Helpers        
def source_generator(size=6, chars=string.ascii_uppercase + string.digits):  
    return ''.join(random.choice(chars) for x in range(size)) 

def target_generator(size=6, chars=string.digits):  
    return '_'.join(random.choice(chars) for x in range(size)) 

          