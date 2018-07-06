from django.views.generic import View
from ..models import Comment, Post
from ..forms import CreateComment
from django.urls import reverse
from django.shortcuts import redirect


class CreateComments(View):
    def post(self, request, **kwargs):
        form = CreateComment(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post.objects.get(pk=kwargs['pk'])
            result = Comment.objects.create(text=data['text'], post=post,
                                            user=request.user)

            result.save()
            return redirect(reverse('blog:view_post', kwargs={'pk': kwargs['pk']}))
