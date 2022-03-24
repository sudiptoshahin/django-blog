
from django.urls import path
from blog import views
from blog.views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # path('', views.home, name='blog-home'),


    # ''' name='blog-about
    # we cann access those path in url with those name
    # those are the url name
    # {% url 'blog-about' %}

    # '''

    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='blog-about'),
]