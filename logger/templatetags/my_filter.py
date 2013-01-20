from django import template
register = template.Library()
@register.filter(name="loads")
def json_loads(value,args):
    return loads(value)


