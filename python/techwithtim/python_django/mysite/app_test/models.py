from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class BlogContent(models.Model):
    fk_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField()

    def __str__(self):
        return self.content

### Python Shell inside Django

'''
python manage.py shell

>>>

Adding Objects

from app_test.models import Blog, BlogContent
blog_title = Blog(title="Malcolmania")
blog_title.save()

>>> Blog.objects.all()
Blog.objects.get(id=1)

blog_title.blogcontent_set.all()
blog_title.blogcontent_set.create(
    author="Malcolm",
    content="Just some blog with a twist or something"
    complete=False
)
blog_title.blogcontent_set.all() # <-- will return only self.content in shell


'''