from django.shortcuts import render

from apps.products.models import Category


def menu_categories(request):
    categories = Category.objects.all()

    return {'menu_categories': categories}
