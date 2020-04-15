from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Exercise Create a new path to a page called new
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New products')
