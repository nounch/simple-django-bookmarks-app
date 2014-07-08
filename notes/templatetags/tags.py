from django import template

register = template.Library()


@register.filter(name='mul')
def mul(value, arg):
    """Filter that multiplies a value with a given parameter.
    Does not do appropriate type checking or error handling.
    """
    print '+' * 80, value
    return value * int(arg)

