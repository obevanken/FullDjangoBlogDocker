from django.views.generic import View, DeleteView, UpdateView
from ..models import Comment, Post
from ..forms import CreateComment, EditFormComment
from django.urls import reverse, reverse_lazy
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


class DeleteComment(DeleteView):
    model = Comment
    template_name = "comment_confirm_delete.html"
    success_url = reverse_lazy('blog:index')


class EditComment(UpdateView):
    model = Comment
    form_class = EditFormComment
    template_name = "edit_comment.html"

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:view_post', kwargs={'pk': self.object.post.pk})


class CreateAnswere(View):
    def post(self, request, **kwargs):
        form = CreateComment(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment.objects.get(pk=kwargs['pk'])
            result = Comment.objects.create(text=data['text'], post=comment.post,
                                            user=request.user, parent=comment)

            result.save()
            return redirect(reverse('blog:view_post', kwargs={'pk': comment.post.id}))
