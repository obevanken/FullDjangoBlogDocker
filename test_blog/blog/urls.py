from django.urls import path
from .views import (Index, LoginAuth, Register, Verify, CreatePost, ViewPost,
                    LogOutView, VotesView, EditPost)
from django.contrib.auth.decorators import login_required
from .models import Post, LikeDislike

app_name = "blog"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', LoginAuth.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('verify/<uuid>/', Verify.as_view(), name='verify'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('post/<int:pk>/', ViewPost.as_view(), name="view_post"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('post/<int:pk>/like/', login_required(VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE))),
    path('post/<int:pk>/dislike/', login_required(VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE))),
    path('post/<int:pk>/edit', EditPost.as_view(), name="editPost"),

]
