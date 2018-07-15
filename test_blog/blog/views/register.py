from django.shortcuts import render, redirect
from ..models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from ..forms import RegistationForm
from django.contrib import messages
from django.views.generic import FormView


class Register(FormView):
    template_name = "register.html"
    form_class = RegistationForm

    def form_valid(self, form):
        data = form.cleaned_data
        result = authenticate(username=data['username'],
                              password=data['password'])

        if result is None:
            print("зашел")
            messages.info(self.request, ' ПОДДТВЕРДИСЬ НА ПОЧТЕ ')
            user = User.objects.create_user(data['username'], data['email'],
                                            data['password'])
            user.save()
            print(user)
            return reverse('blog:login')
