# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader, RequestContext

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("Details of ques: %s" % question_id)

def results(request, question_id):
    return HttpResponse("Results of ques: %s" % question_id)

def votes(request, question_id):
    return HttpResponse("Votes of ques: %s" % question_id)
