# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Word
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.utils import timezone
from googletrans import Translator
from .forms import NameForm

idioms = {'Spanish': 'es', 'English': 'en', 'German': 'de', 'Japanese': 'ja', 'Portuguese': 'pt', 'Russian': 'ru'}

# Create your views here.
def index(request):
    latest_word_list = Word.objects.order_by('-pub_date')[0:10]
    template = loader.get_template('wordstore/index.html')
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            idiom_selected = request.POST['idiom_select']
            print(idiom_selected)
            code_idiom = idioms[idiom_selected]
            # process the data in form.cleaned_data as required
            # translator = Translator()
            # translate = translator.translate(word_intro, dest=code_idiom).text
            word_intro = form.cleaned_data['word_info']
            translate = 'traduccion'
            date = timezone.now()
            Word.objects.create(word = word_intro, translation = translate, pub_date = date)

            # redirect to a new URL:
            form = NameForm()
            context = {
                'latest_word_list': latest_word_list,
                'form': form
            }
            return HttpResponse(template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        context = {
            'latest_word_list': latest_word_list,
            'form': form
        }
        return HttpResponse(template.render(context, request))

def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    return render(request, 'wordstore/detail.html', {'word': word})

def login(request):
    template = loader.get_template('wordstore/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

