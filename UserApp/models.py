from django.db import models
from AdminApp.models import *
# Create your models here.
class UserModel(models.Model):
    User_id = models.AutoField(primary_key=True,default=None)
    Username = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="Active")

    def __str__(self):
        return self.Username

    class Meta:
        db_table = "User_table"

class UserImageModel(models.Model):
    Image_id = models.AutoField(primary_key=True,default=None)
    Image =models.ImageField(upload_to="image")
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)



    class Meta:
        db_table = "UserImage_table"

class OrderModel(models.Model):
    Order_id = models.AutoField(primary_key=True,default=None)
    Quantity = models.IntegerField()
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    Variant_product_id = models.ForeignKey(VariantProductModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Active")



    class Meta:
        db_table = "Order_table"

class ReviewRatingModel(models.Model):
    Review_id = models.AutoField(primary_key=True,default=None)
    Review = models.CharField(max_length=50)
    Rating = models.IntegerField()
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE,null=True)
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Review

    class Meta:
        db_table ="Review_Rating_table"

class AddressModel(models.Model):
    Address_id = models.AutoField(primary_key=True,default=None)
    House_Name = models.CharField(max_length=50)
    House_Number = models.CharField(max_length=50)
    Place = models.CharField(max_length=50)
    Post = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=50)
    Landmark = models.CharField(max_length=50)
    User_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.House_Name

    class Meta:
        db_table = "Address_table"



class CartModel(models.Model):
    Cart_id = models.AutoField(primary_key=True)
    Quantity = models.CharField(max_length=50)
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)



    class Meta:
        db_table = "Cart_table"

class WishlistModel(models.Model):
    Wishlist_id = models.AutoField(primary_key=True)
    User_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)



    class Meta:
        db_table = "WishlistModel_table"







