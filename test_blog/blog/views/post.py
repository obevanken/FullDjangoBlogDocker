from django.shortcuts import render, redirect
from ..forms import PostForm, PostEditForm, CreateComment
from ..models import Post, Comment
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, View, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from ..mixins import PermissonForPostActionMixin


class CreatePost(FormView):
    template_name = "create_post.html"
    form_class = PostForm

    def form_valid(self, form, **kwargs):
        data = form.cleaned_data
        result = Post.objects.create(title=data['title'], text=data['text'],
                                     user=self.request.user, image=data['image'])

        result.save()
        print(result)
        return redirect(reverse('blog:view_post', kwargs={'pk': result.id}))


class ViewPost(View):
    template_name = "view_post.html"

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CreateComment()
        comments = Comment.objects.filter(post=post)

        post.views += 1
        post.save()

        return render(request, self.template_name, {
                                                    'post': post,
                                                    'form': form,
                                                    'comments': comments
                                                    })


class EditPost(PermissonForPostActionMixin, UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = "create_post.html"

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:view_post', kwargs={'pk': self.object.pk})


class DeletePost(PermissonForPostActionMixin, DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy('blog:index')
