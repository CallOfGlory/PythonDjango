from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_full_info, name='movie_full_info'),
    path('movie/<int:movie_id>/short/', views.movie_short_info, name='movie_short_info'),
    path('movie/<int:movie_id>/add-actor/', views.add_movie_actor, name='add_movie_actor'),
    path('movie/add/', views.add_movie, name='add_movie'),
    path('actor/<int:actor_id>/', views.actor_info, name='actor_info'),
    path('actors/', views.actor_list, name='actor_list'),
    path('actor/add/', views.add_actor, name='add_actor'),
]
