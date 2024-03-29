# from django.shortcuts import render

# # proj
# from django.http import HttpResponse, HttpResponseRedirect
# from .models import ToDoList, Item

# from .forms import CreateNewList

# # Create your views here.

# # # proj
# # def index(response, id):
# #     ls = ToDoList.objects.get(id=id)
# #     return render(response, 'main/list.html', {'ls': ls})

# '''Custom Forms'''   
# def index(response, id):
#     ls = ToDoList.objects.get(id=id)

#     if response.method == 'POST':
#         print(response.POST)
#         if response.POST.get('save'): # button name
#             for item in ls.item_set.all():
#                 if response.POST.get('c' + str(item.id)) == 'clicked':
#                     item.complete = True
#                 else:
#                     item.complete = False

#                 item.save()


#         elif response.POST.get('newItem'):
#             txt = response.POST.get('new') # input box name

#             if len(txt) > 2:
#                 ls.item_set.create(text=txt, complete=False)
#             else:
#                 print('invalid')

#     return render(response, 'main/list.html', {'ls': ls})


# def home(response):
#     return render(response, 'main/home.html', {'name': 'test'})

# def create(response):

#     response.user 
    
#     # Checking for post or get request
    
#     if response.method == "POST":
#         form = CreateNewList(response.POST)

#         if form.is_valid():
#             n = form.cleaned_data['name']
#             t = ToDoList(name=n)
#             t.save()

#         return HttpResponseRedirect('/%i' % t.id)
#     else:
#         form = CreateNewList()

#     return render(response, 'main/create.html', {'form': form})


# User Specific pages

from django.shortcuts import render

# proj
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item

from .forms import CreateNewList

# Create your views here.

# # proj
# def index(response, id):
#     ls = ToDoList.objects.get(id=id)
#     return render(response, 'main/list.html', {'ls': ls})

'''Custom Forms'''   
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == 'POST':
            print(response.POST)
            if response.POST.get('save'): # button name
                for item in ls.item_set.all():
                    if response.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()


            elif response.POST.get('newItem'):
                txt = response.POST.get('new') # input box name

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print('invalid')

        return render(response, 'main/list.html', {'ls': ls})
    
    return render(response, 'main/view.html', {})
     


def home(response):
    return render(response, 'main/home.html', {'name': 'test'})

def create(response):

    response.user 
    
    # Checking for post or get request
    
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect('/%i' % t.id)
    else:
        form = CreateNewList()

    return render(response, 'main/create.html', {'form': form})


def view(response):
    return render(response, 'main/view.html', {})