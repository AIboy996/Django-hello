from atexit import register
from django import template

register = template.Library()

@register.filter(name='sqrt')
def sqrt(value, arg):
    return pow(value, 1/arg)

@register.simple_tag
def product(v1, v2, v3):
    return v1*v2*v3

