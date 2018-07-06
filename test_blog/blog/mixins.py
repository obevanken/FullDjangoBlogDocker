from .models import Post
from django.shortcuts import redirect


class PermissonForPostActionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        if request.user.id != post.user.id:
            return redirect("blog:index")
        else:
            return super(PermissonForPostActionMixin, self).dispatch(request, *args, **kwargs)
