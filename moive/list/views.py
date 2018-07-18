from django.shortcuts import render

# Create your views here.
from index.models import Movie, MovieAreas, MovieTypes


def list_html(request):
    if request.method == 'GET':
        return render(request, 'list.html')


def list_html_views(request, letter):
    if request.method == 'GET':
        all_movie = []
        if letter == '0':
            letter = list('0123456789')
            for i in letter:
                movies = Movie.objects.filter(letter=i)
                if movies:
                    for movie in movies:
                        all_movie.append(movie)
            num = len(all_movie)
        else:
            movies = Movie.objects.filter(letter=letter)
            for movie in movies:
                all_movie.append(movie)
            num = len(all_movie)
        areas = MovieAreas.objects.all()
        types = MovieTypes.objects.all()
        data = {
            'all_movie': all_movie,
            'num': num,
            'types': types,
            'areas': areas
        }
        return render(request, 'list.html', data)


def search(request):

    if request.method == 'POST':
        search_name = request.POST.get('Search')
        areas = MovieAreas.objects.all()
        types = MovieTypes.objects.all()
        all_movie = Movie.objects.filter(name__contains=search_name)
        num = len(all_movie)
        data = {
            'all_movie': all_movie,
            'num': num,
            'types': types,
            'areas': areas
        }
        return render(request, 'search.html', data)

