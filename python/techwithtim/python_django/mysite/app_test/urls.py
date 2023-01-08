from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/<int:id>', views.blog_useid, name='blogid'),
    path('blog/<str:title>', views.blog_usetitle, name='blogtitle')
]