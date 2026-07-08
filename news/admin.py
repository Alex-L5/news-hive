from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
# from .models import Blog

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
    # list_display = ('title', 'author', 'created_at', 'votes')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'slug', 'status', 'created_on',)  # 'created_on'
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)  # 'created_on'
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
# admin.site.register(Post)  # create, update and delete news posts
admin.site.register(Comment)
