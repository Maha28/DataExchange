from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import resolve, reverse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def source(request):
    return render(request, 'source.html')