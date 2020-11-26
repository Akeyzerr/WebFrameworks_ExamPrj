from django import template

register = template.Library()


@register.filter
def post_preview(contents, cutoff):
    content = contents[:cutoff] + " ..."
    return content if len(contents) > 140 else contents
