from django.shortcuts import render

## Custom
from django.http import HttpResponse

# Create your views here.
def myView(request):
    return HttpResponse('Hello, Word!')