from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.inclusion_tag('header_component.html', takes_context=True)
def header_component(context, active):
    return {
        "active": active,
        "is_login": context['is_login'],
        "client": context['client']
    }


@register.filter
@stringfilter
def first_char(value):
    return value[0]
