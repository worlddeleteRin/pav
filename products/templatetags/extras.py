from django import template

from products.models import * 

register = template.Library()


@register.simple_tag

def get_first_image(item):
    return item.itemimage_set.all()[0]

@register.simple_tag
def modify_imgurl(imgurl):
    imgurl = imgurl.split('/')[-1]
    imgurl = '/static/images/products/' + imgurl
    return imgurl
