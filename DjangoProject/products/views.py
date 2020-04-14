from django.http import HttpResponse
from django.shortcuts import render


# Exercise Create a new path to a page called new
def index(request):
    return HttpResponse('Hello World')


def new(request):
    return HttpResponse('New products')
