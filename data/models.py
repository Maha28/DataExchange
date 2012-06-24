import random, string
from django.db import models
import pdb

#Constants
MAX_RANDOM_ENTRIES = 20

#Source 
class SourcesManager(models.Manager):
    def addNewSource(self):
        new_source = Sources()
        new_source.save() 
        return new_source.pk   
    
class Sources(models.Model):
    objects = SourcesManager()
    
class SourceManager(models.Manager):
    def populate_source(self, source_id):
        source_instance = Sources.objects.get(pk = source_id)
        for i in range(0,MAX_RANDOM_ENTRIES):
            source = Source(A=source_generator(2),B=source_generator(2), sources = source_instance)
            source.save()     
    
    def clear_source(self, source_id):
        Source.objects.filter(pk = source_id).delete()
        
    def clear_all_sources(self):    
        for source in self.all():
            self.clear_source(source.pk)
        
class Source (models.Model):  
    objects = SourceManager()
    A = models.CharField(max_length=5)
    B = models.CharField(max_length=5)          
    sources = models.ForeignKey(Sources)
    class Meta:
        unique_together = ('A', 'B')      

#Mapping
class MappingManager(models.Manager):
    
    def populate_mapping(self):
        S = []
        T = []
        for source_element in Source.objects.all():
            #Adding Source elements
            appending_multiple_times_based_on_random(S, 1, 4, source_element.A)
            appending_multiple_times_based_on_random(S, 1, 4, source_element.B)
            #Adding Target elements
            appending_multiple_times_based_on_random(T, 1, 4, target_generator(2))
            appending_multiple_times_based_on_random(T, 1, 4, target_generator(2))
        #pdb.set_trace()
        for i in range(0,len(S)):
            try:
                mapping = Mapping(S=S[i],T=T[i])
                mapping.save()
            except: 
                continue
    
    
    def clear_mapping(self):
        Mapping.objects.all().delete()

class Mapping(models.Model):
    objects = MappingManager()
    S = models.CharField(max_length=5)
    T = models.CharField(max_length=5) 
    class Meta:
        unique_together = ('S', 'T')          
    
#Target    
class Target(models.Model):
    X = models.CharField(max_length=5)
    Y = models.CharField(max_length=5)  
    class Meta:
        unique_together = ('X', 'Y')   

#DOM
class Dom(models.Model):
    dom = list()
    
    def generate_dom(self, Source, mapping):
        for source_element in Source.objects.all():
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
        
#Equal        
class EqualManager(models.Manager):
    dom = Dom() 
    current_objects_count = -1
    mapping = Mapping
    
    def get_dom(self):
        return self.dom.get_dom()
    
    def rule_8(self):
        for dom in self.get_dom():
            new_equal = Equal(I=dom, J=dom)
            try:
                new_equal.save()
            except: 
                continue
            
    def rule_9(self):
        for equal_element in Equal.objects.all():
            new_equal = Equal (I=equal_element.J, J=equal_element.I)
            try:
                new_equal.save()
            except: 
                continue
                
    def rule_10(self):
        for equal_element1 in Equal.objects.all():            
            for equal_element2 in Equal.objects.all():            
                if equal_element1.J == equal_element2.I:
                    new_equal = Equal (I=equal_element1.I, J=equal_element2.J) 
                    try:                               
                        new_equal.save() 
                    except: 
                        continue                 
             
    def rule_11(self):
        for mapping_element1 in self.mapping.objects.all():            
            for mapping_element2 in self.mapping.objects.all():
                if mapping_element1.T == mapping_element2.T:
                    new_equal = Equal (I=mapping_element1.S, J=mapping_element2.S) 
                    try:                  
                        new_equal.save()
                    except: 
                        continue        
    
    def rule_12(self):
        for mapping_element1 in self.mapping.objects.all():            
            for mapping_element2 in self.mapping.objects.all(): 
                if mapping_element1.S == mapping_element2.S:  
                    new_equal = Equal (I=mapping_element1.T, J=mapping_element2.T) 
                    try:
                        new_equal.save()                  
                    except: 
                        continue    
                    
    def rule_13(self):      
        for mapping_element in self.mapping.objects.all():
            for equal_element1 in Equal.objects.all():
                if mapping_element.S == equal_element1.I:
                    for equal_element2 in Equal.objects.filter(I=mapping_element.S):
                        new_mapping = Mapping(S=equal_element1.J, T=equal_element2.J)
                        try:
                            new_mapping.save()
                        except: 
                            continue
                    
    def rule_14(self):
        for equal_element in Equal.objects.all():
            for source_element in Source.objects.all():
                if source_element.A == equal_element.I:
                    new_source = Source(A=equal_element.J, B=source_element.B, sources=source_element.sources)
                    try:
                        new_source.save()
                    except: 
                        continue                               

    def not_exausted(self, new_objects_count):
        if self.current_objects_count is new_objects_count:
            return False
        else:
            self.current_objects_count = new_objects_count
            return True
        
    def generate_equal(self):
        while self.not_exausted(Equal.objects.all().count()):
            self.dom.generate_dom(Source, self.mapping)
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
    I = models.CharField(max_length=5)
    J = models.CharField(max_length=5)
    class Meta:
        unique_together = ('I', 'J')    
        
#Helpers        
def source_generator(size=6, chars=string.ascii_uppercase + string.digits):  
    return ''.join(random.choice(chars) for x in range(size)) 

def target_generator(size=6, chars=string.digits):  
    return '_'.join(random.choice(chars) for x in range(size)) 

def appending_multiple_times_based_on_random(rlist, start, end, element):
        random_number = int(random.uniform(start,end))
        for i in range(1,random_number):
            rlist.append(element)



          