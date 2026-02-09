from django.db import models
from django.contrib.auth.models import User  # Import models to connect

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_posts"
    )                                                               # This is a one-to-many or Foreign Key
    content = models.TextField()                                    # This is the news article content
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

