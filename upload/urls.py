from django.conf.urls import url
from upload import views

urlpatterns = [
    url(r'^$', views.form, name = 'upload'),
    url(r'^complete/', views.complete, name = 'complete'),
]
