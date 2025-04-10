from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def deneme(request):
    return HttpResponse("This page is checking for process is true")