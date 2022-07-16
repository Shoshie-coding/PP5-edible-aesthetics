from django.shortcuts import render
from products.models import *

# Create your views here.
def index(request):
    """ A view to return the index page """
    popular_products = Product.objects.filter(count__gt=0).order_by('count')[:5]
     
    return render(request, 'home/index.html', {'popular_products': popular_products})

 