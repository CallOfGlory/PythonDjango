from django.urls import reverse, NoReverseMatch

from .models import Category


def categories_nav(request):
    items = []
    for cat in Category.objects.all():
        try:
            url = reverse('category_detail', args=[cat.slug])
        except NoReverseMatch:
            url = '#'
        items.append({'name': cat.name, 'url': url, 'slug': cat.slug})
    return {'nav_categories': items}