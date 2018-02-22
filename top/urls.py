from django.conf.urls import url
from top import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
