from django.shortcuts import redirect
from ..models import User
from django.http import Http404
from django.views.generic import View


class Verify(View):

    def get(self, request, uuid):
        try:
            user = User.objects.get(verification_uuid=uuid)
        except User.DoesNotExist:
            raise Http404("User does not exist or is already verified")

        user.is_active = True
        user.save()
        print('Работаааааееет')
        return redirect('/')
