from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),    # path('', views.home, name='home'),
]

# urlpatterns = [
    # path('', views.index, name='index'),
    # path('post/<int:post_id>/', views.post_detail, name='post_detail'),
# ]
# Main djangonews/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('news.urls')),
# ]