from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, BlogContent

# Create your views here.

def index(response):
    return HttpResponse('<h1>Test Application without model</h1>')


def blog_useid(response, id):
    bt = Blog.objects.get(id=id)
    content = bt.blogcontent_set.get(id=2)
    return HttpResponse('<h1>%s</h1><br/><h3>Author: %s</h3><br/><p>%s<p>' % (bt.title, content.author, content.content))


def blog_usetitle(response, title):
    bt = Blog.objects.get(title=title)
    content = bt.blogcontent_set.get(id=3)
    return HttpResponse('<h1>%s</h1><br/><h3>Author: %s</h3><br/><p>%s<p>' % (bt.title, content.author, content.content))

