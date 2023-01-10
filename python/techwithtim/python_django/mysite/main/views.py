from django.shortcuts import render

# proj
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

# proj
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'main/list.html', {'ls': ls})


def home(response):
    return render(response, 'main/home.html', {'name': 'test'})
