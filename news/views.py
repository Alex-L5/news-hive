from django.shortcuts import render  # , redirect, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from .models import Post
# from django.contrib.auth.decorators import login_required
# import json
# import os
# from django.shortcuts import render

# def load_posts():
    # file_path = os.path.join(os.path.dirname(__file__), 'news_data.json')
    # with open(file_path, 'r') as file:
        # posts = json.load(file)
    # return posts

# def index(request):
    # posts = load_posts()
    # posts = sorted(posts, key=lambda x: x['votes'], reverse=True)
    # return render(request, 'news/index.html', {'posts': posts})

# def post_detail(request, post_id):
    # post = get_object_or_404(Post, id=post_id)
    # comments = post.comment_set.all()
    # posts = load_posts()
    # post = next((p for p in posts if p["id"] == post_id), None)
    # return render(request, 'news/post_detail.html', {
        # 'post': post,
        # 'comments': comments
    # })                                     # return render(request, 'news/post_detail.html', {'posts': posts})

# @login_required
# def upvote_post(request, post_id):
    # post = get_object_or_404(Post, id=post_id)
    # post.score += 1
    # post.save()
    # return redirect('home')                 # 'index'

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.all()
    # template_name = "post_list.html"  # no difference whether you have the line commented out or not
# def news(request):
    # return HttpResponse("Hello, news!")
    template_name = "news/index.html"
    paginate_by = 6
