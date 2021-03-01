from modeltranslation.translator import translator, TranslationOptions
from .models import Item, Category

class ItemTranslationOption(TranslationOptions):
    fields = (
        'name',
        'eksterier',
        'interier',
        'doors',
        'floor',
        'electrik',
    )

class CategoryTranslationOption(TranslationOptions):
    fields = (
        'name',
    )

translator.register(Item, ItemTranslationOption)
translator.register(Category, CategoryTranslationOption)