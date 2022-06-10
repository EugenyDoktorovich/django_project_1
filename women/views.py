from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.

def index(request): #HttpRequest
    return HttpResponse('Страница приложения women.')

def categories(request, catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home',permanent=True)#параметр дает 301 редирект, без него 302
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')