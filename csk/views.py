from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ruturaj(request):
    return HttpResponse('<h1>captain of csk is ruturaj</h1>')