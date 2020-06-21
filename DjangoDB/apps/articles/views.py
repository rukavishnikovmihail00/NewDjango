from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as BS

from .models import Article, Comment # Импортировали модели (классы)

def index(request):
    #return render(request, 'articles/list.html')
    #return render(request, 'articles/firstpage.html')
    pass

def home(request):
    return HttpResponse('This is a main page')
    #return render(request, 'articles/Computer Vision.html')

def news(request):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.6.0.905 Yowser/2.5 Safari/537.36'
    r = requests.get('https://yandex.ru/', headers = {'User-Agent': user_agent})
    main_text = r.text
    soup = BS(main_text)

    temp = soup.find('div', {'id':'news_panel_news'})
    count = 0

    news = []
    refs = []
    for el in temp.findAll('a', {'area-label':''}):
        news.append(el.text)
        refs.append(el.get('href'))

        count += 1
        if (count == 5):
            break

    return HttpResponse(news)
   
        

    

    