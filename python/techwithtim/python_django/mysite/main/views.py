from django.shortcuts import render

# proj
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

# proj
def index(response, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=2)
    return HttpResponse('<h1>%s</h1><br><br><p>%s</p>' % (ls.name, str(item.text)))
