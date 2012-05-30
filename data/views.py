from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render
from data import models

def home(request):
    return render(request, 'home.html')

def source(request):
    context = {}
    source1 = models.Source1.objects.get_source1()
    source2 = models.Source2.objects.get_source2()
    source3 = models.Source3.objects.get_source3()
    context['source1'] = source1
    context['source2'] = source2  
    context['source3'] = source3  
    return render(request, 'source.html', context)

def mapping(request):
    context = {}
    mapping = models.Mapping.objects.get_mapping()
    context['mapping'] = mapping 
    return render(request, 'mapping.html',context)

def equal(request):
    context = {}
    equal = models.Equal()
    equal.objects.generate_equal()
    context['dom_elements'] = dom.get_elements() 
    context['equal_elements'] = dom.get_elements() 
    return render(request, 'equal.html',context)

def target(request):
    return render(request, 'target.html')

def database(request):
    return render(request, 'database.html')

def populate_source(request):
    models.Source1.objects.populate_source()
    messages.success(request, "You have successfully populated the source tables")
    return HttpResponseRedirect(reverse('database'))    

def clear_source(request):
    models.Source1.objects.clear_source()
    messages.success(request, "You have successfully cleared the source tables")
    return HttpResponseRedirect(reverse('database'))    

def populate_mapping(request):
    models.Mapping.objects.populate_mapping()
    messages.success(request, "You have successfully populated the mapping tables")
    return HttpResponseRedirect(reverse('database'))    

def clear_mapping(request):
    models.Mapping.objects.clear_mapping()
    messages.success(request, "You have successfully cleared the mapping tables")
    return HttpResponseRedirect(reverse('database'))  

