from django.db import models
from django.contrib.auth.models import User  # Import models to connect
# import json
# from posts.models import Post

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # url = models.URLField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_posts"
    )                                                               # This is a one-to-many or Foreign Key
    content = models.TextField()                                    # This is the news article content
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)
    # score = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_on"]

    # @property
    # def score(self):
        # return self.upvotes - self.downvotes

        def __str__(self):
            return f"{self.title} | written by {self.author}"  # def __str__(self):
                                                                   # return self.title

        # def loaddata(filepath):

        # with open('news_posts.json', 'r') as f:
            # data = json.load(f)
        # for item in data:
            # Post.objects.create(
                # title=item['title'],
                # content=item['content'],
                # excerpt=item['excerpt']
            # )


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    # parent = models.ForeignKey(
        # 'self', null=True, blank=True, on_delete=models.CASCADE
    # )
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"  # return self.content[:30]

    # post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
        # return f"Comment by {self.author}"