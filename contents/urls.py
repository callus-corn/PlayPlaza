from django.conf.urls import url

from .views import ContentsListView

app_name = 'contents'
urlpatterns = [
    url(r'^$', ContentsListView.as_view(template_name='contents/list.html')),
]
