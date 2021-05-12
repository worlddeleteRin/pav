#!/usr/bin/env python3


import pandas as pd
import numpy as np
import os
import pandas as pd
import requests
import base64

import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pav.settings')
django.setup()

from products.models import *

brand_img_path = 'static/images/'
products_img_path = 'static/images/products/'
products_data_path = "/Users/noname/work/ilya/goods/goods_final_translated_test.xlsx"


def createProducts():
    deleteall()
    print('-------------------------')
    print('starting create products')
    print('-------------------------')
    index = 0
    data = pd.read_excel(products_data_path)
    for index, item in data.iterrows():
        name = item['name']
        name_en = item['name_en']
        name_ua = item['name_ua']
        name_ge = item['name_de']
        name_tr = item['name_tr']
        price = item['price']
        price = price.replace('от', '').strip()
        price = int(price)
        category_name = item['category']
        category_name_en = item['category_en']
        category_name_ua = item['category_ua']
        category_name_ge = item['category_de']
        category_name_tr = item['category_tr']
        size = item['size']
        h_in = item['h_in']
        h_out = item['h_out']
        eksterier = item['eksterier']
        eksterier_en = item['eksterier_en']
        eksterier_ua = item['eksterier_ua']
        eksterier_ge = item['eksterier_de']
        eksterier_tr = item['eksterier_tr']
        interier = item['interier']
        interier_en = item['interier_en']
        interier_ua = item['interier_ua']
        interier_ge = item['interier_de']
        interier_tr = item['interier_tr']
        doors = item['doors']
        doors_en = item['doors_en']
        doors_ua = item['doors_ua']
        doors_ge = item['doors_de']
        doors_tr = item['doors_tr']
        floor = item['floor']
        floor_en = item['floor_en']
        floor_ua = item['floor_ua']
        floor_ge = item['floor_de']
        floor_tr = item['floor_tr']
        electrik = item['electrik']
        electrik_en = item['electrik_en']
        electrik_ua = item['electrik_ua']
        electrik_ge = item['electrik_de']
        electrik_tr = item['electrik_tr']
        
        category_imgurl = item['category_imgurl']

        category = Category.objects.get_or_create(
            name = category_name,
            name_en = category_name_en,
            name_uk = category_name_ua,
            name_ge = category_name_ge,
            name_ru = category_name, 
            name_tr = category_name_tr, 
            imgurl = category_imgurl,
        )[0]    

        print(category.id, category.name)
        print(price, type(price))

        new_item = Item(
            category = category,
            name = name,
            name_en = name_en,
            name_uk = name_ua,
            name_ge = name_ge,
            name_tr = name_tr,
            name_ru = name,
            price = price,
            size = size,
            h_in = h_in,
            h_out = h_out,
            eksterier = eksterier,
            eksterier_en = eksterier_en,
            eksterier_uk = eksterier_ua,
            eksterier_ge = eksterier_ge,
            eksterier_tr = eksterier_tr,
            eksterier_ru = eksterier,
            interier = interier,
            interier_en = interier_en,
            interier_uk = interier_ua,
            interier_ge = interier_ge,
            interier_tr = interier_tr,
            interier_ru = interier,
            doors = doors,
            doors_en = doors_en,
            doors_uk = doors_ua,
            doors_ge = doors_ge,
            doors_tr = doors_tr,
            doors_ru = doors,
            floor = floor,
            floor_en = floor_en,
            floor_uk = floor_ua,
            floor_ge = floor_ge,
            floor_tr = floor_tr,
            floor_ru = floor,
            electrik = electrik,
            electrik_en = electrik_en,
            electrik_uk = electrik_ua,
            electrik_ge = electrik_ge,
            electrik_tr = electrik_tr,
            electrik_ru = electrik,
        )
        print(new_item.name_ge)
        new_item.save()

        imgurl = item['imgurl']
        if type(imgurl) == str:
            imgurl = imgurl.split(',')


        for dire, file, item in os.walk(products_img_path):
            for i in item:
                i_norm = i.split('.')[0]
                if type(imgurl) == list:
                    print('find list variable')
                    print(imgurl)
                    for im in imgurl:
                        im = str(im)
                        im = im.strip()
                        print('subimage', im)
                        if im == str(i_norm):
                            print('cool, it passed')
                            print('it passed', im)
                            item_name = i
                            new_imgurl = item_name
                            new_item_image = Itemimage(
                                item = new_item,
                                imgurl = new_imgurl,
                            )
                            print('new item image is:')
                            new_item_image.save()
                            # print(new_item_image)
                else:
                    if str(imgurl).strip() == str(i_norm):
                            print('it passed', imgurl)
                            item_name = i
                            imgurl = item_name
                            new_item_image = Itemimage(
                                item = new_item,
                                imgurl = imgurl,
                            )
                            new_item_image.save()

        
        print('his index was', index)
    print('created', index, 'products')




def createall():
    createProducts()

if __name__ == "__main__":
    createall()