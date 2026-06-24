from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovieForm, ReviewForm
from .models import Genre, Movie, Review

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

    movies = Movie.objects.select_related('genre').all().order_by(field)

    def toggle_dir(key):
        return 'desc' if (sort == key and direction == 'asc') else 'asc'

    sort_links = {key: f'?sort={key}&dir={toggle_dir(key)}' for key in SORT_OPTIONS}

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'current_sort': sort,
        'current_dir': direction,
        'sort_links': sort_links,
    })


def movie_detail(request, pk):
    movie = get_object_or_404(Movie.objects.select_related('genre'), pk=pk)
    reviews = movie.reviews.all()
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'review_count': reviews.count(),
    })


def review_create(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.username = _next_username()
            review.save()
            messages.success(request, f'Відгук від {review.username} додано!')
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = ReviewForm()
    return render(request, 'movies/review_form.html', {'form': form, 'movie': movie})


def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    movie_pk = review.movie_id
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Відгук видалено.')
        return redirect('movie_detail', pk=movie_pk)
    return render(request, 'movies/review_confirm_delete.html', {'review': review})


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


def _next_username():
    import re
    used = set()
    pattern = re.compile(r'^testUser(\d+)$')
    for name in Review.objects.values_list('username', flat=True):
        m = pattern.match(name)
        if m:
            used.add(int(m.group(1)))
    n = 0
    while n in used:
        n += 1
    return f'testUser{n}'