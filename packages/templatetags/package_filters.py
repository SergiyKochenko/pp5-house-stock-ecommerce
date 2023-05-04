from django import template
register = template.Library()


@register.filter(name='split')
def split_filter(text, delimiter):
    if text is not None:
        return text.split(delimiter)
    else:
        return ''
