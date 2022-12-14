from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem

# def todoView(request):
#     return render(request, 'todo.html')


## to view items from todo_todoitem
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
    {
        'all_items': all_todo_items
    })