from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404

from account.models import User


class QuitView(DeleteView):
    model = User
    success_url = '/'

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)
