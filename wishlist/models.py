from django.db import models


from products.models import Product
from profiles.models import UserProfile
# Create your models here.


class Wishlist(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist(), on_delete=models.SET_NULL,null=True, blank=True)
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)