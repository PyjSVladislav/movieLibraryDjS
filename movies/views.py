from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie

class MovieView(View):
    '''List of Movies'''

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movie_list.html', {'movie_list': movies})

class MovieDetail(View):
    '''Detail of Movie'''

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movies/movie_detail.html',{'movie': movie})