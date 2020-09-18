from django.template import library

register = library.Library()


@register.filter
def first(obj):
    pass

# @register.simple_tag
# def create_the_queue(req):
