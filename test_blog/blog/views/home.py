from django.views.generic import View
from ..models import Post
from django.shortcuts import render


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template_name, {'posts': posts})
