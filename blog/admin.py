from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin # defines the text editor, enabling you to access its functionality in the admin panel for your posts.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)} # In the prepopulated_fields, the tuple containing the single value of title requires a trailing comma.
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
