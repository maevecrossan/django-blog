from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) #applies filter to database  
    template_name = "blog/index.html" #use this to change template name
    paginate_by = 6 # displays six posts at a time
