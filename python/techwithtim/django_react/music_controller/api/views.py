from django.shortcuts import render

# App
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.

# # App
# def main(request):
#     return HttpResponse('<h1>Hello</h1>')

# # Shows Room View with a Form
# class RoomView(generics.CreateAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer

# Show ROom view with only a list
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


