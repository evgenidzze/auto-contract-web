from django import template

register = template.Library()


@register.filter
def range_filter(items, range_str):

    if items is None:
        return []
    start, end = map(int, range_str.split(':'))

    return items[start - 1:end]


@register.filter
def get_type(value):
    return type(value)


@register.filter
def get_img(value):
    return str(value)
