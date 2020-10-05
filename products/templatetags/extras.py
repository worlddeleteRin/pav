from django import template

from products.models import * 

register = template.Library()


@register.simple_tag

def get_first_image(item):
    return item.itemimage_set.all()[0]