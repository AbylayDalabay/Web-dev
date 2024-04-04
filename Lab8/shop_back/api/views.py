from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category


# Create your views here.

def products_list(request):
    products = [product.to_json() for product in Product.objects.all()]
    data = {
        'product': products

    }
    return JsonResponse(data, status=200)


def get_product(request, id):
    try:
        product = Product.objects.get(id)
        return JsonResponse(product.to_json(), status=200)
    except Product.DoesNotExist as error:
        return JsonResponse(error, status=400)


def categories_list(request):
    categories = [category.to_json() for category in Category.objects.all()]
    data = {
        'catagories': categories
    }
    return JsonResponse(data, status=200)


def get_category(request, id):
    try:
        category = Category.objects.get(id)
        return JsonResponse(category.to_json(), status=200)
    except Category.DoesNotExist as error:
        return JsonResponse(error, status=400)


def products_list_by_categories(request, id):
    products = [product.to_json() for product in Product.objects.filter(id)]
    data = {
        'products': products
    }
    return JsonResponse(data, status=200)
