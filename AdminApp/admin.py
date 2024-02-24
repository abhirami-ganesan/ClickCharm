from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AdminModel)
admin.site.register(MainCategoryModel)
admin.site.register(SubCategoryModel)
admin.site.register(SubSubCategoryModel)
admin.site.register(ProductModel)
admin.site.register(ProductImageModel)
admin.site.register(VariantProductModel)
admin.site.register(OfferEventModel)
admin.site.register(OfferModel)
admin.site.register(DistrictModel)
admin.site.register(CityModel)
admin.site.register(BrandModel)
