from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}

]

def index(request):
    posts = Product.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Google'
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about.html')


def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Войти')

