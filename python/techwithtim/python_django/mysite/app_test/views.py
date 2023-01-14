from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, BlogContent

from .forms import CreateNewBlog

# Create your views here.

# '''Before Templates'''

# def index(response):
#     return HttpResponse('<h1>Test Application without model</h1>')


# def blog_useid(response, id):
#     bt = Blog.objects.get(id=id)
#     content = bt.blogcontent_set.get(id=2)
#     return HttpResponse('<h1>%s</h1><br/><h3>Author: %s</h3><br/><p>%s<p>' % (bt.title, content.author, content.content))


# def blog_usetitle(response, title):
#     bt = Blog.objects.get(title=title)
#     content = bt.blogcontent_set.get(id=3)
#     return HttpResponse('<h1>%s</h1><br/><h3>Author: %s</h3><br/><p>%s<p>' % (bt.title, content.author, content.content))



''' Using Templates'''
def home(response):
    return render(response, 'app_test/home.html', {'name': 'home'})

# def blog(response, id):
#     bl = Blog.objects.get(id=id)
#     return render(response, 'app_test/blog.html', {'blog': bl})


'''Using Custom Forms'''
def blog(response, id):
    bl = Blog.objects.get(id=id)

    if response.method == 'POST':
        print(response.POST)

        if response.POST.get('save'):
            for author in bl.blogcontent_set.all():
                if response.POST.get(str(author.id)) == 'clicked':
                    author.complete = True
                else:
                    author.complete = False

                author.save()


        elif response.POST.get('newAuthor'):
            txt = response.POST.get('authorName')

            if len(txt) > 2:
                bl.blogcontent_set.create(author=txt, complete=False)
            else:
                print('Invalid!!!!')
    
    return render(response, 'app_test/blog.html', {'blog': bl})


''' Using Forms '''

# # Basic Level
# def create(response):

#     form = CreateNewBlog()
#     return render(response, 'app_test/create.html', {'form': form})

# Adjusted Level
def create(response):

    if response.method == "POST":
        form = CreateNewBlog(response.POST)

        if form.is_valid():
            new = form.cleaned_data['title']
            title = Blog(title=new)
            title.save()

        return HttpResponseRedirect('/app_test/blog/%i' % title.id)

    else:
        form = CreateNewBlog()
        
    return render(response, 'app_test/create.html', {'form': form})