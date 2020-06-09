from django.shortcuts import render

from .models import Article, Comment # Импортировали модели (классы)

def index(request):
    #return render(request, 'articles/list.html')
    return render(request, 'articles/firstpage.html')