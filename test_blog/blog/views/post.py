from django.shortcuts import render, redirect
from ..forms import PostForm, PostEditForm
from ..models import Post
from django.urls import reverse
from django.views.generic import FormView, View, UpdateView
from django.shortcuts import get_object_or_404


class CreatePost(FormView):
    template_name = "create_post.html"
    form_class = PostForm

    def form_valid(self, form):
        data = form.cleaned_data
        result = Post.objects.create(title=data['title'], text=data['text'],
                                     user=self.request.user, image=data['image'])

        result.save()
        print(result)
        return redirect('/post/{0}'.format(result.id))


class ViewPost(View):
    template_name = "view_post.html"

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        post.views += 1
        post.save()

        return render(request, self.template_name, {'post': post})


class EditPost(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = "create_post.html"

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:view_post', kwargs={'pk': self.object.pk})

    def get(self, request, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        if request.user.id != post.user.id:
            return redirect("blog:index")
        else:
            return super(self.__class__, self).get(request, **kwargs)
