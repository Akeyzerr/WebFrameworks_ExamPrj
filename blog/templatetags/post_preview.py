from django import template

register = template.Library()


@register.filter
def post_preview(contents, cutoff):
    content = contents[:cutoff] + " ..."
    return content if len(contents) > cutoff else contents
