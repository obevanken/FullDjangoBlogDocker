from ..models import User
from ..forms import UserEditForm
from ..mixins import PermissonForUserActionMixin
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404


class ViewUser(View):
    template_name = "view_user.html"

    def get(self, request, uuid):
        user = get_object_or_404(User, verification_uuid=uuid)
        return render(request, self.template_name, {'us': user, 'posts': user.posts.all()})


class EditUser(PermissonForUserActionMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "edit_user.html"

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:view_user', kwargs={'uuid': self.object.verification_uuid})


class DeleteUser(PermissonForUserActionMixin, DeleteView):
    model = User
    template_name = "user_confirm_delete.html"
    success_url = reverse_lazy('blog:index')
