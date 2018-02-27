from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import DeleteContentView, ContentListView

app_name = 'delete'
urlpatterns = [
    url(r'^$', login_required(ContentListView.as_view(template_name='delete/list.html'))),
    url(r'^(?P<pk>\d+)/$', login_required(DeleteContentView.as_view(template_name='delete/form.html'))),
]
