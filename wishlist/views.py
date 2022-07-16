from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import *
from products.models import *
from django.contrib import messages

# Create your views here.

from django.views.decorators.http import require_POST

@require_POST
def add(request):  

    redirect_url = request.POST.get('redirect_url')
    if request.user.is_authenticated:
        
        profile = UserProfile.objects.get(user=request.user)
        try:
            wl = Wishlist.objects.get(user_profile=profile)
        except:
            wl = Wishlist(user_profile=profile)
            wl.save()
        p = Product.objects.get(pk=request.POST['id'])
       
        try:
            WishlistItem.objects.get(wishlist=wl, product=p)
        except:

            wish_list_item = WishlistItem(wishlist=wl, product=p)
            wish_list_item.save()

        messages.success(request, f'Added to your wishlist')
    return redirect(redirect_url)
        

@require_POST
def remove(request):  

    redirect_url = request.POST.get('redirect_url')
    if request.user.is_authenticated:
        
        profile = UserProfile.objects.get(user=request.user)
        try:
            wl = Wishlist.objects.get(user_profile=profile)
        except:
            wl = Wishlist(user_profile=profile)
            wl.save()
        p = Product.objects.get(pk=request.POST['id'])
       
    
        wi = WishlistItem.objects.get(wishlist=wl, product=p)
        wi.delete()
     

        messages.success(request, f'Removed from your wishlist')
    return redirect(redirect_url)
        


