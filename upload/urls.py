from django.conf.urls import url
from upload import views

app_name = 'upload'
urlpatterns = [
    url(r'^$', views.form, name = 'upload'),
    url(r'^complete/', views.complete, name = 'complete'),
]
