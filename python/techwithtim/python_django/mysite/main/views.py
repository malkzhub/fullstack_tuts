from django.shortcuts import render

# proj
from django.http import HttpResponse

# Create your views here.

# proj
def index(response):
    return HttpResponse('<h1>Moga Tech Industries.</h1>')

def v1(response):
    return HttpResponse('<h1>View 1!</h1>')