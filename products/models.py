from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(default='', max_length = 200)
    imgurl = models.ImageField(upload_to='static/images', blank = True, null = True)

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, )
    name = models.CharField(default='', max_length = 300)
    price = models.IntegerField(default=0,)
    size = models.CharField(default='', max_length = 300)
    h_in = models.CharField(default='', max_length = 300)
    h_out = models.CharField(default='', max_length = 300)
    eksterier = models.CharField(default='', max_length = 300)
    interier = models.CharField(default='', max_length = 300)
    doors = models.CharField(default='', max_length = 300)
    floor = models.CharField(default='', max_length = 300)
    electrik = models.CharField(default='', max_length = 300)
    imgurl = models.ImageField (upload_to='static/images/products', blank = True, null = True)


def deleteall():
    c = Category.objects.all()
    i = Item.objects.all()
    i.delete()
    c.delete()
    print('deleted all')
