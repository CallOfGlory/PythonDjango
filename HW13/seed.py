import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_collection.settings')
django.setup()

from movies.models import Genre, Movie, Review

GENRES = ['Бойовик', 'Драма', 'Фантастика', 'Фентезі', 'Трилер']

MOVIES = [
    ('Початок', 'Крістофер Нолан', date(2010, 7, 16), 'Злодій, який викрадає секрети через спільні сни.', 5, 'Фантастика'),
    ('Інтерстеллар', 'Крістофер Нолан', date(2014, 11, 7), 'Подорож крізь простір і час заради людства.', 5, 'Фантастика'),
    ('Матриця', 'Вачовскі', date(1999, 3, 31), 'Програміст дізнається, що реальність — симуляція.', 4, 'Бойовик'),
    ('Гаррі Поттер і філософський камінь', 'Кріс Коламбус', date(2001, 11, 29), 'Хлопчик-чаклун дізнається правду про своє походження.', 4, 'Фентезі'),
    ('Володар перснів: Хранителі Персня', 'Пітер Джексон', date(2001, 12, 19), 'Початок епічної подорожі до знищення Персня.', 5, 'Фентезі'),
    ('Гладіатор', 'Рідлі Скотт', date(2000, 5, 5), 'Римський полководець стає гладіатором.', 4, 'Драма'),
    ('Паразити', 'Пон Чжун Хо', date(2019, 5, 30), 'Бідна родина проникає в життя заможної сім\'ї.', 5, 'Трилер'),
]

REVIEWS = {
    'Початок': ['Неймовірний сюжет, дивився тричі!', 'Шедевр!'],
    'Інтерстеллар': ['Фільм, що змінює світогляд.'],
    'Матриця': ['Культова класика.', 'Трохи застарілі спецефекти, але ідея — вогонь.'],
}

for name in GENRES:
    Genre.objects.get_or_create(name=name)

for title, director, release, desc, rating, genre_name in MOVIES:
    genre = Genre.objects.get(name=genre_name)
    movie, _ = Movie.objects.get_or_create(
        title=title,
        defaults={
            'director': director,
            'release_date': release,
            'description': desc,
            'rating': rating,
            'genre': genre,
        },
    )
    for idx, text in enumerate(REVIEWS.get(title, [])):
        Review.objects.get_or_create(
            movie=movie,
            username=f'testUser{idx}',
            defaults={'text': text},
        )

print('Жанрів:', Genre.objects.count(), '| Фільмів:', Movie.objects.count(), '| Відгуків:', Review.objects.count())