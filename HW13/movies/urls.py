from django.urls import path

from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('create/', views.movie_create, name='movie_create'),
    path('<int:pk>/', views.movie_detail, name='movie_detail'),
    path('<int:pk>/edit/', views.movie_update, name='movie_update'),
    path('<int:pk>/delete/', views.movie_delete, name='movie_delete'),
    path('<int:pk>/review/add/', views.review_create, name='review_create'),
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),
]