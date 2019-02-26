# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def company(request):
    return render(request, 'core/company.html')

def game(request):
    return render(request, 'core/game.html')

def contact(request):
    return render(request, 'core/contact.html')

def news(request):
    return render(request, 'core/news.html')
