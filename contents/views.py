from django.views.generic import ListView

from .models import Content

class ContentsListView(ListView):
    model = Content
