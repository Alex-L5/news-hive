from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),    # path('', views.home, name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]

# urlpatterns = [
    # path('', views.index, name='index'),
    # path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('upvote/<int:post_id>/', views.upvote, name='upvote'),
# ]                                                                     # views.upvote_post, name='upvote_post
# Main djangonews/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('news.urls')),
# ]