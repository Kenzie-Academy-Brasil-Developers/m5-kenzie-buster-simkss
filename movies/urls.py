from django.urls import path
from . import views

urlpatterns = [
    path("", views.MovieViews.as_view()),
    path("<int:movie_id>/", views.MovieDetailViews.as_view()),
    path("<int:movie_id>/orders/", views.MovieOrderView.as_view())
    ]