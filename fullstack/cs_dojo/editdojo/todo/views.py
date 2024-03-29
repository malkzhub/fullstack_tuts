from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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

def addTodo(request):
    # create a new todo all_items
    # save
    # redirect the browser to '/todo/'
    
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')