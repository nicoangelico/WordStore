# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Word
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.utils import timezone
from googletrans import Translator
from .forms import NameForm
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

idioms = {'Spanish': 'es', 'English': 'en', 'German': 'de', 'Japanese': 'ja', 'Portuguese': 'pt', 'Russian': 'ru'}

def index(request):
    template = loader.get_template('wordstore/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def userWord(request):
    latest_word_list = Word.objects.filter(created_by=request.user).order_by('-pub_date')
    template = loader.get_template('wordstore/userword.html')
    
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
            word_intro = form.cleaned_data['word_info']
            translator = Translator()
            translate = translator.translate(word_intro, dest=code_idiom).text
            date = timezone.now()
            user = request.user
            Word.objects.create(word = word_intro, translation = translate, pub_date = date, created_by = user)

            # redirect to a new URL:
            paginator = Paginator(latest_word_list, 10) # Show 10 contacts per page
            page = request.GET.get('page')
            try:
                words_list = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                words_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                words_list = paginator.page(paginator.num_pages)

            context = {
                'words_list': words_list,
                'form': form
            }
            return HttpResponse(template.render(context, request))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

        #Pagination
        paginator = Paginator(latest_word_list, 10) # Show 10 contacts per page
        page = request.GET.get('page')
        try:
            words_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            words_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            words_list = paginator.page(paginator.num_pages)

        context = {
            'words_list': words_list,
            'form': form
        }
        return HttpResponse(template.render(context, request))

def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    return render(request, 'wordstore/detail.html', {'word': word})

def newUser(request):
    template = loader.get_template('wordstore/login.html')
    context = {}
    return HttpResponse(template.render(context, request))