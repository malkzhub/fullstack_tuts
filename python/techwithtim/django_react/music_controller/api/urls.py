# App

from django.urls import path
# from .views import main
from .views import RoomView

# urlpatterns = [
#     path('home/', main),
#     path('', main)
# ]

urlpatterns = [
    path('roomgi/', RoomView.as_view()),
]
