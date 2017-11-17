# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'webapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'webapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'webapp/result.html'

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('webapp/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'webapp/index.html', context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'webapp/detail.html', {'question': question})

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'webapp/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'webapp/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #Request.POST es un objeto similar a un diccionario que le permite acceder
        #a los datos enviados por nombre de clave. En este caso, request.POST ['choice']
        #devuelve el ID de la elección seleccionada, como una cadena. request.POST 
        #valores son siempre cadenas.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'webapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('webapp:results', args=(question.id,)))