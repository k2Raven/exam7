from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from webapp.models import Poll


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll


class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    model = Poll
    fields = ['question']

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})
