from django.urls import path
from . import views

# these are the paths that we type in in order to go to the correct part of the site
# it reads
# 8000/products
# 8000/products/new
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]