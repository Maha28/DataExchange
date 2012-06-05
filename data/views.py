from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render
from data import models

def home(request):
    return render(request, 'home.html')

def source(request):
    context = {}
    context['source1'] = models.Source1.objects.all()
    context['source2'] = models.Source2.objects.all()  
    context['source3'] = models.Source3.objects.all()  
    return render(request, 'source.html', context)

def mapping(request):
    context = {}
    context['mapping'] = models.Mapping.objects.all() 
    return render(request, 'mapping.html',context)

def equal(request):
    context = {}
    context['dom'] = models.Equal.objects.get_dom()
    context['equal'] = models.Equal.objects.all()
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

def generate_equal(request):
    models.Equal.objects.generate_equal()
    messages.success(request, "You have successfully generated Equal")
    return HttpResponseRedirect(reverse('database'))    

def clear_equal(request):
    models.Equal.objects.clear_equal()
    messages.success(request, "You have successfully cleared Equal")
    return HttpResponseRedirect(reverse('database'))  

def clear_all(request):
    models.Source1.objects.clear_source()
    models.Mapping.objects.clear_mapping()
    models.Equal.objects.clear_equal()
    messages.success(request, "You have successfully cleared everything")
    return HttpResponseRedirect(reverse('database'))  

#The following methods are temporary copied to accomplish a small task.
#TODO: Use arguments to combine these views with the old ones
def populate_source_from_source(request):
    models.Source1.objects.populate_source()
    messages.success(request, "You have successfully populated the source tables")
    return HttpResponseRedirect(reverse('source'))    

def clear_source_from_source(request):
    models.Source1.objects.clear_source()
    messages.success(request, "You have successfully cleared the source tables")
    return HttpResponseRedirect(reverse('source')) 

def populate_mapping_from_mapping(request):
    models.Mapping.objects.populate_mapping()
    messages.success(request, "You have successfully populated the mapping tables")
    return HttpResponseRedirect(reverse('mapping'))    

def clear_mapping_from_mapping(request):
    models.Mapping.objects.clear_mapping()
    messages.success(request, "You have successfully cleared the mapping tables")
    return HttpResponseRedirect(reverse('mapping'))  

def generate_equal_from_equal(request):
    models.Equal.objects.generate_equal()
    messages.success(request, "You have successfully generated Equal")
    return HttpResponseRedirect(reverse('equal'))   

def clear_equal_from_equal(request):
    models.Equal.objects.clear_equal()
    messages.success(request, "You have successfully cleared Equal")
    return HttpResponseRedirect(reverse('equal'))  
