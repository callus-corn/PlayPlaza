from django.views.generic import CreateView

from account.models import User
from .forms import UserCreationForm

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "form.html"
    success_url = "/"
