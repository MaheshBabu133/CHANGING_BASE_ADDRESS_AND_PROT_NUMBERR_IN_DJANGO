from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def First(request):
    return HttpResponse('<center><h1>This is  my First django project</h1></center>')