from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Actor, MovieActor


def movie_full_info(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    actors = movie.movie_actors.all()
    return render(request, 'movies/movie_full_info.html', {
        'movie': movie,
        'actors': actors
    })


def movie_short_info(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/movie_short_info.html', {'movie': movie})


def actor_info(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    roles = actor.movie_roles.all()
    return render(request, 'movies/actor_info.html', {
        'actor': actor,
        'roles': roles
    })


def movie_list(request):
    movies = Movie.objects.all().order_by('-release_year')
    return render(request, 'movies/movie_list.html', {'movies': movies})


def actor_list(request):
    actors = Actor.objects.all().order_by('full_name')
    return render(request, 'movies/actor_list.html', {'actors': actors})


def add_movie(request):
    if request.method == 'POST':
        movie = Movie.objects.create(
            title=request.POST.get('title'),
            genre=request.POST.get('genre'),
            director=request.POST.get('director'),
            release_year=request.POST.get('release_year'),
            duration=request.POST.get('duration'),
            studio=request.POST.get('studio'),
            description=request.POST.get('description', '')
        )
        return redirect('movie_full_info', movie_id=movie.id)
    return render(request, 'movies/add_movie.html')


def add_actor(request):
    if request.method == 'POST':
        actor = Actor.objects.create(
            full_name=request.POST.get('full_name'),
            birth_date=request.POST.get('birth_date'),
            biography=request.POST.get('biography', ''),
            photo_url=request.POST.get('photo_url', '')
        )
        return redirect('actor_info', actor_id=actor.id)
    return render(request, 'movies/add_actor.html')


def add_movie_actor(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        actor_id = request.POST.get('actor_id')
        role = request.POST.get('role')
        actor = get_object_or_404(Actor, id=actor_id)
        MovieActor.objects.create(movie=movie, actor=actor, role=role)
        return redirect('movie_full_info', movie_id=movie.id)

    actors = Actor.objects.all()
    return render(request, 'movies/add_movie_actor.html', {'movie': movie, 'actors': actors})
