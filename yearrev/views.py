from django.shortcuts import render, redirect

from yearrev.forms import *
from .models import *
from django.db.models import Q

def base(request):
    return render(request, 'base.html')

def anime(request,pk):
    query = pk
    if query is not None:
        lookups = Q(startyear__icontains=query)
        results =Anime.objects.filter(lookups)
        print(results)
        context = {'results': results, }
    return render(request, 'anime.html', context)

def animeadd(request):
    if request.method == 'GET':
        form = Animeform()
    else:
        form = Animeform(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            form = Animeform()
            return redirect('animeyear')
    return render(request, 'animeadd.html',{'form':form})

def movie(request,pk):
    query = pk
    if query is not None:
        lookups = Q(year__icontains=query)
        results = Movie.objects.filter(lookups)
        print(results)
        context = {'results': results, }
    return render(request, 'movie.html', context)

def movieadd(request):
    if request.method == 'GET':
        form = Movieform()
    else:
        form = Movieform(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            form =  Movieform()
            return redirect('movieyear')
    return render(request, 'movieadd.html',{'form':form})

def game(request):
    return render(request, 'game.html',{'game':game})

def manga(request):
    manga = Manga.objects.all()
    return render(request, 'manga.html',{'manga':manga})

def book(request):
    book = Book.objects.all()
    return render(request, 'book.html',{'book':book})

def moviesyear(request):
        return render(request, 'moviesyear.html')


def animeyear(request):
    return render(request, 'animeyear.html')
def gameyear(request):
    return render(request, 'gameyear.html')
def game2019(request):
    return render(request, 'gameyear2019.html')
def game2018(request):
    return render(request, 'gameyear2018.html')
def editanime(request):
    return render(request, 'animeedit.html')
def drawingyear(request):
    return render(request, 'drawingyear.html')

def drawing(request,pk):
    query = pk
    if query is not None:
        lookups = Q(year__icontains=query)
        results = Drawing.objects.filter(lookups)
        print(results)
        context = {'results': results, }
    return render(request, 'drawing2020.html', context)

def cookingyear(request):
    return render(request, 'cookingyear.html')


