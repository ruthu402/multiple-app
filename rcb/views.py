from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h3><marquee>captain of rcb is virat</marquee></h3>')