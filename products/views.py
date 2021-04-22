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
from django.utils import translation


# Create your views here.

def set_current_language_cookie(request, lang_code):
    user_language = lang_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
def get_current_language(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        return request.session[translation.LANGUAGE_SESSION_KEY]
    else:
        return None
def set_current_language(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        user_language = request.session[translation.LANGUAGE_SESSION_KEY]
        translation.activate(user_language)
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language


def index(request):
    set_current_language(request)
    items = Item.objects.all()
    categories = Category.objects.all()

    # lang = request.session[translation.LANGUAGE_SESSION_KEY]
    lang = get_current_language(request)
    return render(request, 'products/index.html', {
        'items': items,
        'categories': categories,
        'lang': lang,
    })

def category(request, cat_id):
    set_current_language(request)
    
    current_category = Category.objects.get(id = cat_id)
    items = Item.objects.filter(category__id = cat_id)
    print(items)
    return render(request, 'products/category.html', {
        'category': current_category,
        'items': items,
    })

def item(request, item_id):
    set_current_language(request)

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

    # try:
    print('start sending')
    send_mail(
            'Заявка на обратный звонок!',
            htmlt_email_plain,
            'mafstroygarant@mail.ru',
            # EMAIL_HOST_USER,
            [
            'maf.stroy1@gmail.com', 
            # 'worlddelete0@yandex.ru'
            ],
            html_message = html_email
            )  
    print('send')
    # except:
    #     pass
    return JsonResponse({

    }, status = 200)

def set_language_ajax(request):
    lang_code = request.GET['lang_code']
    print('lang code is', lang_code)
    set_current_language_cookie(request, lang_code)
    success = True
    return JsonResponse({
        'success': success
    }, status = 200)