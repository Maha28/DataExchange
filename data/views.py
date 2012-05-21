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
    #source2 = request.user.get_traveller().get_requests()
    #source3 = request.user.get_traveller().get_requests()
    context['source1'] = source1
    #context['source2'] = source2  
    #context['source3'] = source3  
    return render(request, 'source.html', context)

def mapping(request):
    return render(request, 'mapping.html')

def target(request):
    return render(request, 'target.html')

def database(request):
    return render(request, 'database.html')

def populate_source(request):
    models.Source1.objects.populate_source()
    messages.success(request, "You have successfully populated the source tables")
    return HttpResponseRedirect(reverse('database'))    