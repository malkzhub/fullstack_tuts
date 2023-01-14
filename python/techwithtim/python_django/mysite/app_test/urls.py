from django.urls import path
from . import views

# ''' Not Using Templates'''

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('blog/<int:id>', views.blog_useid, name='blogid'),
#     path('blog/<str:title>', views.blog_usetitle, name='blogtitle')
# ]


''' Using Templates '''
urlpatterns =[
    path('', views.home, name='home'),
    path('blog/<int:id>', views.blog, name='blog'),
    path('create/', views.create, name='create'),
]