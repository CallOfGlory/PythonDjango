from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovieForm
from .models import Movie

SORT_OPTIONS = {
    'title': 'title',
    'rating': 'rating',
    'release_date': 'release_date',
}


def movie_list(request):
    sort = request.GET.get('sort', 'title')
    direction = request.GET.get('dir', 'asc')
    field = SORT_OPTIONS.get(sort, 'title')
    if direction == 'desc':
        field = '-' + field

    movies = Movie.objects.all().order_by(field)

    def toggle_dir(key):
        return 'desc' if (sort == key and direction == 'asc') else 'asc'

    sort_links = {
        key: f'?sort={key}&dir={toggle_dir(key)}' for key in SORT_OPTIONS
    }

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'current_sort': sort,
        'current_dir': direction,
        'sort_links': sort_links,
    })


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            messages.success(request, f'Фільм «{movie.title}» додано!')
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Додати фільм'})


def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, f'Фільм «{movie.title}» оновлено!')
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Редагувати фільм'})


def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        title = movie.title
        movie.delete()
        messages.success(request, f'Фільм «{title}» видалено!')
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})