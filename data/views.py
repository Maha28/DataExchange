from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render

from data import models

def home(request):
    return render(request, 'home.html')

def source(request):
    return render(request, 'source.html')

def mapping(request):
    return render(request, 'mapping.html')

def target(request):
    return render(request, 'target.html')

def database(request):
    return render(request, 'database.html')

def populate_source(request):
    pass