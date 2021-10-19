from django import template

register = template.Library()

def sliceLast(value, n):
    """Returns the last n values of a list and excludes the first"""
    #return value.replace(arg, '')
    return value[max(1, len(value)-int(n)):]

register.filter('sliceLast', sliceLast)
