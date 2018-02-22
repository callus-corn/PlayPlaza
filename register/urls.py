from django.conf.urls import url

from .views import UserCreateView

urlpatterns = [
    url(r'^$', UserCreateView.as_view()),
]
