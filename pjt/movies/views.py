from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


def new(request):

    return render(request, 'movies/new.html')


def edit(request, pk):
    movie  = Movie.objects.get(pk=pk)
    Genre = movie.genre
    
    context = {
        'movie' : movie,
        'Genre' : Genre,
    }
    return render(request, 'movies/edit.html', context)

def update(request, pk):
    movie  = Movie.objects.get(pk=pk)

    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.score = request.POST.get('score')

    movie.save()

    return redirect('movies:index')
    

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie,

    }
    return render(request, 'movies/detail.html', context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

def create(request):

    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    score = request.POST.get('score')

    movie = Movie(title=title, score=score, audience=audience, release_date=release_date, genre=genre, poster_url=poster_url, description=description)
    movie.save()
    return redirect('movies:index')