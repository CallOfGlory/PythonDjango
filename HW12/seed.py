import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_collection.settings')
django.setup()

from movies.models import Movie

MOVIES = [
    ('Початок', 'Крістофер Нолан', date(2010, 7, 16), 'Злодій, який викрадає секрети через спільні сни.', 5),
    ('Інтерстеллар', 'Крістофер Нолан', date(2014, 11, 7), 'Подорож крізь простір і час заради людства.', 5),
    ('Матриця', 'Вачовскі', date(1999, 3, 31), 'Програміст дізнається, що реальність — симуляція.', 4),
    ('Гаррі Поттер і філософський камінь', 'Кріс Коламбус', date(2001, 11, 29), 'Хлопчик-чаклун дізнається правду про своє походження.', 4),
    ('Володар перснів: Хранителі Персня', 'Пітер Джексон', date(2001, 12, 19), 'Початок епічної подорожі до знищення Персня.', 5),
    ('Гладіатор', 'Рідлі Скотт', date(2000, 5, 5), 'Римський полководець стає гладіатором.', 4),
    ('Паразити', 'Пон Чжун Хо', date(2019, 5, 30), 'Бідна родина проникає в життя заможної сім\'ї.', 5),
]

for title, director, release, desc, rating in MOVIES:
    Movie.objects.get_or_create(
        title=title,
        defaults={
            'director': director,
            'release_date': release,
            'description': desc,
            'rating': rating,
        },
    )

print('Фільмів у базі:', Movie.objects.count())