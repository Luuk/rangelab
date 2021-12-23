from django import template

register = template.Library()

@register.filter
def format_upload_url(value):
    return str(value).replace('app/static/', '')