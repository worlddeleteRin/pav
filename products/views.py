from django.shortcuts import render
from .models import * 
from django.http import JsonResponse, HttpResponse
import urllib
import os
from django.core.files.storage import default_storage
from pav.settings import * 
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/index.html', {
        'items': items,
        'categories': categories,
    })

def category(request, cat_id):
    current_category = Category.objects.get(id = cat_id)
    items = Item.objects.filter(category__id = cat_id)
    print(items)
    return render(request, 'products/category.html', {
        'category': current_category,
        'items': items,
    })

def item(request, item_id):
    current_item = Item.objects.get(id = item_id)
    return render(request, 'products/item.html', {
        'item': current_item,
    })


def contact_form_send(request):
    name = request.GET['name']
    name = urllib.parse.unquote(name)
    phone = request.GET['phone']
    phone = urllib.parse.unquote(phone)

    context = {
        'name': name,
        'phone': phone,
    }
    html_email = render_to_string('products/blocks/email_form_template.html', context = context)
    htmlt_email_plain = strip_tags(html_email)

    try:
        send_mail(
                'Заявка на обратный звонок!',
                htmlt_email_plain,
                EMAIL_HOST_USER,
                [
                # 'maf.stroy1@gmail.com', 
                'worlddelete0@yandex.ru'
                ],
                html_message = html_email
                )  
    except:
        pass
    return JsonResponse({

    }, status = 200)



