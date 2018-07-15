from django.urls import path
from .views import (Index, LoginAuth, Register, Verify, CreatePost, ViewPost,
                    LogOutView, VotesView, EditPost, DeletePost, CreateComments,
                    DeleteComment, ViewUser, EditUser, DeleteUser, EditComment,
                    CreateAnswere)
from django.contrib.auth.decorators import login_required
from .models import Post, LikeDislike, Comment

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
    path('comment/<int:pk>/like/', login_required(VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE))),
    path('comment/<int:pk>/dislike/', login_required(VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE))),
    path('post/<int:pk>/edit', EditPost.as_view(), name="editPost"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name="deletePost"),
    path('post/<int:pk>/create_comment', CreateComments.as_view(), name="create_comment"),
    path('comment/<int:pk>/delete', DeleteComment.as_view(), name="delete_comment"),
    path('user/<uuid>', ViewUser.as_view(), name="view_user"),
    path('user/<int:pk>/edit', EditUser.as_view(), name="edit_user"),
    path('user/<int:pk>/delete', DeleteUser.as_view(), name="delete_user"),
    path('comment/<int:pk>/edit', EditComment.as_view(), name="edit_comment"),
    path('answere/<int:pk>/create', CreateAnswere.as_view(), name="create_answere"),

]
