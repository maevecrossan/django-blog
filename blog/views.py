from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) #applies filter to database  
    template_name = "blog/index.html" #use this to change template name
    paginate_by = 6 # displays six posts at a time

def post_detail(request, slug): # looking for the exact blog post clicked on. The slug is passed in to help Django
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1) # looking for published posts
    post = get_object_or_404(queryset, slug=slug) # if Django can't find the post, 404 error
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render( # if the post is found, we use the following template (post_detail.html)
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count
        },
    )