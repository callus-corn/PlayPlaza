from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import QuitView

urlpatterns = [
    url(r'^$', login_required(QuitView.as_view(template_name='quit/form.html'))),
]
