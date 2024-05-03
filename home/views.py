from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return HttpResponse('<h1>this is about page')