from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('news/', views.news, name = 'news')
    #path('', views.index, name = 'index')
    #path('test/', views.test, name = 'test')
]