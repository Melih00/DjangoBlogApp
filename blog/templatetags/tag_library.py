from django import template

register = template.Library()

@register.filter()
def to_int(value):
    return int(value)
@register.filter()
def update123(value):
    """Allows to update existing variable in template"""
    return value