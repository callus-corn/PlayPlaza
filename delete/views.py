from django.views.generic import ListView, DeleteView

from contents.models import Content


class ContentListView(ListView):
    model = Content

    def get_queryset(self):
        return Content.objects.filter(author=self.request.user.id)

class DeleteContentView(DeleteView):
    model = Content
    success_url = '/'
