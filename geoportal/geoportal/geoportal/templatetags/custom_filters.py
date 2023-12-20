from django import template

register = template.Library()

@register.filter(name='first_sentence')
def first_sentence(text):
    sentences = text.split('.')
    return sentences[0] if sentences else ''
