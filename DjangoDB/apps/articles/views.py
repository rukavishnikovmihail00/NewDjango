from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Comment # Импортировали модели (классы)

def index(request):
    #return render(request, 'articles/list.html')
    return render(request, 'articles/firstpage.html')


def home(request):
    return HttpResponse('This is a main page')