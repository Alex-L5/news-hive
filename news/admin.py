from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)                   # create, update and delete news posts
admin.site.register(Comment)