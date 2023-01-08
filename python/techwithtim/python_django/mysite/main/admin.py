from django.contrib import admin

# proj
from .models import ToDoList, Item

# Register your models here.

# proj
admin.site.register(ToDoList)
admin.site.register(Item)
