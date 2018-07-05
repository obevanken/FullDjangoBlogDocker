from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from ..forms import LoginForm
from django.views.generic import FormView


class LoginAuth(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])

        if user is not None:
            login(self.request, user)
            return redirect("/")
        else:
            messages.error(
                self.request, 'Аккаунт не существует или отклонён модератором')
            return self.form_invalid(form)
