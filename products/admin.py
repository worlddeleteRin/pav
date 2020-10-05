from django.contrib import admin
from products.models import * 

# Register your models here.


class ItemiamgeInline(admin.TabularInline):
    model = Itemimage

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemiamgeInline]

admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Itemimage)