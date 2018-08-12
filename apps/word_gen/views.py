# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    request.session['counter'] += 0
    random_word = {"word": get_random_string(length=14)}
    return render(request, "word_gen/index.html", random_word)

def reset(request):
    if request.method == 'POST':
        request.session['counter'] += 1
        return redirect('/')
