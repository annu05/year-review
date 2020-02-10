from django.shortcuts import render, redirect

from yearrev.forms import *
from .models import *

def base(request):
    return render(request, 'base.html')

def anime(request):
    anime = Anime.objects.all()
    return render(request, 'anime.html',{'anime':anime})

def animeadd(request):
    if request.method == 'GET':
        form = Animeform()
    else:
        form = Animeform(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            form = Animeform()
            return redirect('anime')
    return render(request, 'animeadd.html',{'form':form})

def movie(request):
    movie = Movie.objects.all()
    return render(request, 'movie.html',{'movie':movie})

def movieadd(request):
    if request.method == 'GET':
        form = Movieform()
    else:
        form = Movieform(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            form =  Movieform()
            return redirect('movie')
    return render(request, 'movieadd.html',{'form':form})

def game(request):
    return render(request, 'game.html',{'game':game})

def manga(request):
    manga = Manga.objects.all()
    return render(request, 'manga.html',{'manga':manga})

def book(request):
    book = Book.objects.all()
    return render(request, 'book.html',{'book':book})

