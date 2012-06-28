from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render
from data import models
import pdb

#Home
def home(request):
    return render(request, 'home.html')

#Source
def create_new_source(request, view_name):
    source_id = models.Sources.objects.addNewSource() 
    messages.success(request, "You have successfully added a new source with id %i " % source_id )
    if view_name == 'source':
        return HttpResponseRedirect(reverse('source'))  
    else:     
        return HttpResponseRedirect(reverse('database'))   
    
def delete_source(request, view_name, source_id):
    models.Sources.objects.deleteSource(int(source_id)) 
    messages.success(request, "You have successfully deleted the source with id %i " % int(source_id))
    if view_name == 'source':
        return HttpResponseRedirect(reverse('source'))  
    else:     
        return HttpResponseRedirect(reverse('database'))         

def clear_source(request, view_name, source_id):
    models.Source.objects.clear_source(int(source_id))
    messages.success(request, "You have successfully cleared the source with id %i " % int(source_id))
    if view_name == 'source':
        return HttpResponseRedirect(reverse('source'))  
    else:     
        return HttpResponseRedirect(reverse('database'))  

def source(request):
    context = {}
    context['sources'] = models.Sources.objects.all()
    context['source'] = models.Source.objects.all()
    return render(request, 'source.html', context)

def populate_source(request, view_name, source_id):
    models.Source.objects.populate_source(source_id)
    messages.success(request, "You have successfully populated the source with id %i " % int(source_id))
    if view_name == 'source':
        return HttpResponseRedirect(reverse('source'))  
    else:     
        return HttpResponseRedirect(reverse('database'))  



#Mapping
def mapping(request):
    context = {}
    context['mapping'] = models.Mapping.objects.all().order_by('T') 
    return render(request, 'mapping.html',context)

def populate_mapping(request,view_name):
    models.Mapping.objects.populate_mapping()
    messages.success(request, "You have successfully populated the mapping tables")
    if view_name == 'mapping':
        return HttpResponseRedirect(reverse('mapping'))  
    else:     
        return HttpResponseRedirect(reverse('database'))     

def clear_mapping(request,view_name):
    models.Mapping.objects.clear_mapping()
    messages.success(request, "You have successfully cleared the mapping tables")
    if view_name == 'mapping':
        return HttpResponseRedirect(reverse('mapping'))  
    else:     
        return HttpResponseRedirect(reverse('database'))

#Equal
def equal(request):
    context = {}
    context['dom'] = models.Equal.objects.get_dom()
    context['equal'] = models.Equal.objects.all()
    return render(request, 'equal.html',context)

def generate_equal(request,view_name):
    models.Equal.objects.generate_equal()
    messages.success(request, "You have successfully generated Equal")
    if view_name == 'equal':
        return HttpResponseRedirect(reverse('equal'))  
    else:     
        return HttpResponseRedirect(reverse('database'))  

def update_mapping_from_equal(request,view_name):
    models.Equal.objects.rule_13()
    messages.success(request, "You have successfully updated the mapping table using equal")
    if view_name == 'equal':
        return HttpResponseRedirect(reverse('equal'))  
    else:     
        return HttpResponseRedirect(reverse('database'))  

def update_source_from_equal(request,view_name):
    models.Equal.objects.rule_14()
    messages.success(request, "You have successfully updated the source table using equal")
    if view_name == 'equal':
        return HttpResponseRedirect(reverse('equal'))  
    else:     
        return HttpResponseRedirect(reverse('database'))

def clear_equal(request,view_name):
    models.Equal.objects.clear_equal()
    messages.success(request, "You have successfully cleared Equal")
    if view_name == 'equal':
        return HttpResponseRedirect(reverse('equal'))  
    else:     
        return HttpResponseRedirect(reverse('database'))

#Queries
def queries(request):
    context = {}
    context['sources'] = models.Sources.objects.all()   
    context['targets'] = models.Targets.objects.all() 
    if request.method == 'POST':
         models.STDependencies.objects.run_query(request.POST)
         messages.success(request, "You have successfully submited your query")
    return render(request, 'queries.html', context)

#Target
def target(request):
    return render(request, 'target.html')

def create_new_target(request, view_name):
    target_id = models.Targets.objects.addNewTarget() 
    messages.success(request, "You have successfully added a new target with id %i " % target_id )
    if view_name == 'target':
        return HttpResponseRedirect(reverse('target'))  
    else:     
        return HttpResponseRedirect(reverse('database'))   
    
def delete_target(request, view_name, target_id):
    models.Targets.objects.deleteTarget(int(target_id)) 
    messages.success(request, "You have successfully deleted the target with id %i " % int(target_id))
    if view_name == 'target':
        return HttpResponseRedirect(reverse('target'))  
    else:     
        return HttpResponseRedirect(reverse('database')) 
    
def clear_target(request, view_name, target_id):
    models.Target.objects.clear_target(int(target_id))
    messages.success(request, "You have successfully cleared the target with id %i " % int(target_id))
    if view_name == 'target':
        return HttpResponseRedirect(reverse('target'))  
    else:     
        return HttpResponseRedirect(reverse('database'))     

#Database
def database(request):
    context = {}
    context['sources'] = models.Sources.objects.all() 
    context['targets'] = models.Targets.objects.all() 
    return render(request, 'database.html', context)

def clear_all(request):
    models.Source.objects.clear_all_sources()
    models.Mapping.objects.clear_mapping()
    models.Equal.objects.clear_equal()
    messages.success(request, "You have successfully cleared everything")
    return HttpResponseRedirect(reverse('database')) 

def clear_all_sources(request):
    for source in models.sources.objects.all():
        clear_source(source.pk)
        