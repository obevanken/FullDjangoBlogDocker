from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import auth


class LogOutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('/')
