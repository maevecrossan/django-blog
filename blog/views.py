from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

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
    comments = post.comments.all().order_by("-created_on") # retrieves all of the comments for the selected blog post and orders them from newest to oldest. 'comments' comes from related_name in the Comment model.
    comment_count = post.comments.filter(approved=True).count() # filters comments on a post
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid(): # improves the security of our system because, even if an attacker bypasses the front-end form HTML validation, we still check it on the back-end
            comment = comment_form.save(commit=False) # Calling the save method with commit=False returns an object that hasn't yet been saved to the database so that we can modify it further. Called again below.
            comment.author = request.user # sets author to logged in user
            comment.post = post # get_object_or_404 at start of view code
            comment.save() # saved to database once the above fields are populated
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval',
            )

    comment_form = CommentForm() # resets the form so a user can add another comment if they wish.

    return render( # if the post is found, we use the following template (post_detail.html)
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )