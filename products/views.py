from django.shortcuts import render
from .models import * 
from django.http import JsonResponse, HttpResponse
import urllib
import os
from django.core.files.storage import default_storage
from pav.settings import * 

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


