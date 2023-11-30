from django.urls import path, include

from rest_framework import routers

from movies.views import movie_list_view, MovieListView, MovieViewSet

movie_list = MovieViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)


urlpatterns = [
    # path('', movie_list_view, name="movie_list"),
    # path('', MovieListView.as_view(), name='movie_list'),
    path("", movie_list, name="movie_list")
]

app_name = "movies"
