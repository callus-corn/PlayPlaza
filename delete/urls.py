from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import DeleteAccountView

urlpatterns = [
    url(r'^$', login_required(DeleteAccountView.as_view(template_name='delete/form.html'))),
]
