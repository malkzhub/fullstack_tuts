from django.db import models

# custom model
from django.contrib.auth.models import User

# Create your models here.

# # proj
# class ToDoList(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Item(models.Model):
#     todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()

#     def __str__(self):
#         return self.text

# custom models
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
