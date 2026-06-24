import re

from django import template

from ..models import Review

register = template.Library()


@register.simple_tag
def next_username():
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