from django import template

register = template.Library()


@register.filter
def get_words(dictio, lang):
    return dictio.get(lang, ['Seems like there is no any Word yet.'])


@register.filter
def get_translation(dictio, args):
    return dictio.get(args[0]).get(args[1]) if dictio.get(args[0], {})\
        .get(args[1], ['Seems like there is no any Word yet.']) else ['No Translation']
