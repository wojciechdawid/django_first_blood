from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request, name="world"):
    return HttpResponse(f"Hello {name}")