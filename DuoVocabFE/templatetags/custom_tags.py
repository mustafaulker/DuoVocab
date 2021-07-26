from django import template

register = template.Library()


@register.filter
def select_language(h, key):
    return h.get(key, '-')
