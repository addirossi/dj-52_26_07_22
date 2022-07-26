from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def index(request):
    return HttpResponse('Привет, это Нетология!')


def products_list(request):
    products = Product.objects.all()
    return render(request, 'main/list.html', {'products': products})
