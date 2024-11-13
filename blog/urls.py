from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'), # sets a string (ft the slug) as the URL extension  # The slug path converter before the colon defines the data type as a slug, and the slug after the colon is the post.slug value passed from the template. You see this value in the URL path in the browser bar.
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
]