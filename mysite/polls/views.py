# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse
from django.template import loader, RequestContext

# Create your views here.
# def index(request):
#     latest_questions = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_questions': latest_questions}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question,pk = question_id)
#     return render(request,'polls/detail.html',{'question':question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def votes(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    try:
        selected_choice = quetion.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request,'polls/detail.html',{'question':question,'error_messsage':"Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args= (question.id,)))
