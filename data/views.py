from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render
from data import models

#Home
def home(request):
    return render(request, 'home.html')

#Source
def source(request):
    context = {}
    context['source1'] = models.Source1.objects.all()
    context['source2'] = models.Source2.objects.all()  
    context['source3'] = models.Source3.objects.all()  
    return render(request, 'source.html', context)

def populate_source(request, view_name):
    models.Source1.objects.populate_source()
    messages.success(request, "You have successfully populated the source tables")
    if view_name == 'source':
        return HttpResponseRedirect(reverse('source'))  
    else:     
        return HttpResponseRedirect(reverse('database'))  

def clear_source(request, view_name):
    models.Source1.objects.clear_source()
    messages.success(request, "You have successfully cleared the source tables")
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
#Target
def target(request):
    return render(request, 'target.html')

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

#Database
def database(request):
    return render(request, 'database.html')

def clear_all(request):
    models.Source1.objects.clear_source()
    models.Mapping.objects.clear_mapping()
    models.Equal.objects.clear_equal()
    messages.success(request, "You have successfully cleared everything")
    return HttpResponseRedirect(reverse('database')) 
