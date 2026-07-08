from django.db import models
from django.contrib.auth.models import User  # Import models to connect
from cloudinary.models import CloudinaryField
# import json
# from posts.models import Post

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # url = models.URLField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_posts"
    )                               # This is a one-to-many or Foreign Key
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    # votes = models.IntegerField(default=0)
    # score = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    # @property
    # def score(self):
        # return self.upvotes - self.downvotes

    def __str__(self):
        return f"{self.title} | written by {self.author}"  # def __str__(self):


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()

    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
