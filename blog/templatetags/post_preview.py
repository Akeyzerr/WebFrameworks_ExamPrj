from django import template

register = template.Library()


@register.filter
def post_preview(contents):
    return [t[:150] for t in contents]