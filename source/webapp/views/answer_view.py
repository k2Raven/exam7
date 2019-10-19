from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View

from webapp.models import Answer, Poll, Choice


class AnswerView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choices = poll.choice.all()
        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'answer/answer_form.html',context)

    def post(self, request, *args, **kwargs):
        poll = request.POST.get('poll')
        choice = request.POST.get('choice')
        answer = Answer.objects.create(poll=poll, choice=choice)
        answer.save()
        return render(request, 'answer/answer_form.html',context)
