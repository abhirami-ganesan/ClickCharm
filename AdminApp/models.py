from django.db import models

# Create your models here.


class AdminModel(models.Model):
    Admin_id = models.IntegerField(primary_key=True, default=None)
    Admin_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)



    class Meta:
        db_table = "Admin_table"


class MainCategoryModel(models.Model):
    Main_category_id = models.IntegerField(primary_key=True, default=None)
    Main_category = models.CharField(max_length=50)

    def __str__(self):
        return self.Main_category

    class Meta:
        db_table = "MainCategory_table"


class SubCategoryModel(models.Model):
    Sub_category_id = models.IntegerField(primary_key=True, default=None)
    Sub_category = models.CharField(max_length=50)
    Main_category_id = models.ForeignKey(MainCategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Sub_category

    class Meta:
        db_table = "SubCategory_table"


class SubSubCategoryModel(models.Model):
    Sub_sub_category_id = models.IntegerField(primary_key=True, default=None)
    Sub_sub_category = models.CharField(max_length=50)
    Sub_category_id = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Sub_sub_category


    class Meta:
        db_table = "Sub_sub_category_table"

class BrandModel(models.Model):
    Brand_id = models.IntegerField(primary_key=True, default=None)
    image = models.ImageField(upload_to='images/')
    Brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Brand_name

    class Meta:
        db_table = "Brand_table"


class ProductModel(models.Model):
    Product_id = models.AutoField(primary_key=True, default=None)
    Product_title = models.CharField(max_length=50)
    Product_description = models.CharField(max_length=50)
    Quantity = models.IntegerField(null=True)
    Price = models.IntegerField()
    status = models.CharField(max_length=50,default="Active")
    Main_category_id = models.ForeignKey(MainCategoryModel, on_delete=models.CASCADE,null=True)
    Brand_id = models.ForeignKey(BrandModel, on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.Product_title

    class Meta:
        db_table = "Product_table"


class ProductImageModel(models.Model):
    image_id = models.IntegerField(primary_key=True, default=None)
    images = models.ImageField(upload_to='images/')
    Product_id = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE)

    # Admin_id = models.ForeignKey(AdminModel, on_delete=models.CASCADE)


    class Meta:
        db_table = "Product_image_table"


class VariantProductModel(models.Model):
    Variant_product_id = models.IntegerField(primary_key=True, default=None)
    Variant_product_name = models.CharField(max_length=50)
    Size = models.IntegerField()
    Quantity = models.CharField(max_length=50,null=True)
    Color = models.CharField(max_length=50)
    Occasion = models.CharField(max_length=50)
    Neck = models.CharField(max_length=50)
    Bottom_Fabric = models.CharField(max_length=50)
    Top_type = models.CharField(max_length=50)
    Sleeve_Length = models.CharField(max_length=50)
    Top_Fabric = models.CharField(max_length=50)
    Bottom_Type = models.CharField(max_length=50)
    Bottom_Pattern = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    # Admin_id = models.ForeignKey(AdminModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Variant_product_name

    class Meta:
        db_table = "Variant_Product_table"





class OfferEventModel(models.Model):
    Offer_id = models.IntegerField(primary_key=True, default=None)
    Offer_Name = models.CharField(max_length=50)
    Start_Date = models.DateField()
    End_Date = models.DateField()

    def __str__(self):
        return self.Offer_Name


    class Meta:
        db_table = "Offer_Event_table"


class OfferModel(models.Model):
    Event_id = models.IntegerField(primary_key=True, default=None)
    Discount = models.IntegerField()
    Offer_id = models.ForeignKey(OfferEventModel, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)



    class Meta:
        db_table = "Offer_table"


class DistrictModel(models.Model):
    District_id = models.IntegerField(primary_key=True, default=None)
    District_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.District_Name

    class Meta:
        db_table = "District_table"


class CityModel(models.Model):
    City_id = models.IntegerField(primary_key=True, default=None)
    City_Name = models.CharField(max_length=50)
    District_id = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.City_Name

    class Meta:
        db_table = "City_table"

