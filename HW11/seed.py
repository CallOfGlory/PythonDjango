import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')
django.setup()

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile

from news.models import Article, Category

CATEGORIES = [
    ('Політика', 'polityka', (60, 90, 160)),
    ('Спорт', 'sport', (200, 70, 70)),
    ('Технології', 'tehnologii', (50, 130, 90)),
    ('Культура', 'kultura', (140, 90, 160)),
]

ARTICLES = {
    'polityka': [
        ('Парламент ухвалив бюджет на наступний рік', 'Депутати проголосували за основний фінансовий документ країни...'),
        ('Президент провів зустріч з прем’єр-міністром', 'Сторони обговорили ключові питання порядку денного...'),
    ],
    'sport': [
        ('Збірна України перемогла у товариському матчі', 'Наші футболісти здобули впевнену перемогу з рахунком 3:1...'),
        ('Олімпійські ігри: оголошено склад збірної', 'До національної команди увійшли як досвідчені, так і молоді спортсмени...'),
    ],
    'tehnologii': [
        ('Новий чип відкриває епоху енергоефективних пристроїв', 'Виробник обіцяє зменшення енергоспоживання до 40%...'),
        ('Штучний інтелект допомагає лікарям у діагностиці', 'Нейромережі вже використовуються у провідних клініках світу...'),
    ],
    'kultura': [
        ('У Києві відкрилася виставка сучасного мистецтва', 'Експозиція включає понад 80 робіт молодих художників...'),
    ],
}


def make_image(label, color):
    img = Image.new('RGB', (800, 450), color=color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype('arial.ttf', 48)
    except Exception:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), label, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((800 - w) / 2, (450 - h) / 2), label, fill='white', font=font)
    buf = BytesIO()
    img.save(buf, format='JPEG', quality=85)
    return ContentFile(buf.getvalue(), name=f'{label}.jpg')


for name, slug, color in CATEGORIES:
    cat, _ = Category.objects.get_or_create(slug=slug, defaults={'name': name})
    for idx, (title, content) in enumerate(ARTICLES.get(slug, []), start=1):
        article, created = Article.objects.get_or_create(
            category=cat, title=title,
            defaults={'content': content},
        )
        if created or not article.image:
            article.image.save(f'{slug}_{idx}.jpg', make_image(name, color), save=True)

print('Готово:', Category.objects.count(), 'категорій,', Article.objects.count(), 'новин')