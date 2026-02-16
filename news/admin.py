from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
# from .models import Blog

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
    # list_display = ('title', 'author', 'created_at', 'votes')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
# admin.site.register(Post)                   # create, update and delete news posts
admin.site.register(Comment)