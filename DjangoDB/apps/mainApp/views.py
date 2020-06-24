from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Contact me using: ','+79290446585', "rukavishnikovmihail00@yandex.ru"]})