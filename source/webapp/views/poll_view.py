from django.views.generic import ListView

from webapp.models import Poll


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1
