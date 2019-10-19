from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.models import Choice, Poll
from webapp.forms import ChoiceForm


class ChoiceCreateView(CreateView):
    template_name = 'choice/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.choice.create(**form.cleaned_data)
        return redirect('poll_view', pk=poll_pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'choice/delete.html'
    model = Choice
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})