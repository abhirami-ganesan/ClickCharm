from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserModel)
admin.site.register(UserImageModel)
admin.site.register(OrderModel)
admin.site.register(ReviewRatingModel)
admin.site.register(AddressModel)
admin.site.register(CartModel)
admin.site.register(WishlistModel)