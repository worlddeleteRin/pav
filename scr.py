#!/usr/bin/env python3

from products.models import *
import pandas as pd
import numpy as np
import os
import pandas as pd
import requests
import base64

brand_img_path = 'static/images/'
products_img_path = 'static/images/products/'
products_data_path = '/Users/noname/work/ilya/goods/goods.xlsx'


def createProducts():
    deleteall()
    print('-------------------------')
    print('starting create products')
    print('-------------------------')
    index = 0
    data = pd.read_excel(products_data_path)
    for index, item in data.iterrows():
        name = item['name']
        price = item['price']
        price = price.replace('от', '').strip()
        price = int(price)
        category_name = item['category']
        size = item['size']
        h_in = item['h_in']
        h_out = item['h_out']
        eksterier = item['eksterier']
        interier = item['interier']
        doors = item['doors']
        floor = item['floor']
        electrik = item['electrik']
        
        category_imgurl = item['category_imgurl']

        category = Category.objects.get_or_create(
            name = category_name,
            imgurl = category_imgurl,
        )[0]

        print(category.id, category.name)
        print(price, type(price))

        new_item = Item(
            category = category,
            name = name,
            price = price,
            size = size,
            h_in = h_in,
            h_out = h_out,
            eksterier = eksterier,
            interier = interier,
            doors = doors,
            floor = floor,
            electrik = electrik,
        )
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