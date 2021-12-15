from django.urls import path

from .views import MovieDetail, MovieView

urlpatterns = [
    path("", MovieView.as_view(), ),
    path("<slug:slug>/",MovieDetail.as_view(), name = 'movie_detail')
]
