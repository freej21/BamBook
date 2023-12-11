# custom_filters.py

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape

register = template.Library()

@register.filter(name='first_letter_and_hash', is_safe=True, needs_autoescape=True)
@stringfilter
def first_letter_and_hash(value, autoescape=True):
    if not value:
        return ''
    
    if len(value) == 1:
        return value[0] + '***'
    
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    
    return esc(value[0]) + '*' * (len(value) - 1)
