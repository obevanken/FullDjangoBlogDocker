from .models import Post, User
from django.shortcuts import redirect
from django.urls import reverse


class PermissonForPostActionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        if request.user.id != post.user.id:
            return redirect("blog:index")
        else:
            return super(PermissonForPostActionMixin, self).dispatch(request, *args, **kwargs)


class PermissonForUserActionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.kwargs['pk'])
        if request.user.id != user.id:
            return redirect("/user/" + str(user.verification_uuid))
        else:
            return super(PermissonForUserActionMixin, self).dispatch(request, *args, **kwargs)
