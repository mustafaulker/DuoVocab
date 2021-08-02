from django import template

register = template.Library()


@register.filter
def get_words(dictio, lang):
    return dictio.get(lang, '-')


@register.filter
def get_translation(dictio, args):
    return dictio.get(args[0], '-').get(args[1])
