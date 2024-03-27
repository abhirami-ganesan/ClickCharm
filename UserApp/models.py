from django.db import models
from AdminApp.models import *


# Create your models here.
from django.db import models

class UserModel(models.Model):
    """
    Model representing a user.

    Fields:
    - User_id: AutoField, primary key.
    - Username: CharField with a maximum length of 50 characters.
    - Phone_Number: CharField with a maximum length of 50 characters.
    - Password: CharField with a maximum length of 50 characters.
    - status: CharField with a default value of "Active".
    """
    User_id = models.AutoField(primary_key=True, default=None)
    Username = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)



    status = models.CharField(max_length=50, default="Active")


    def __str__(self):
        return self.Username

    class Meta:
        db_table = "User_table"


class UserImageModel(models.Model):
    """
    Model representing a user's image.

    Fields:
    - Image_id: AutoField, primary key.
    - Image: ImageField for storing image uploads.
    - User_id: ForeignKey linking to UserModel.
    """
    Image_id = models.AutoField(primary_key=True, default=None)
    Image = models.ImageField(upload_to="image")
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "UserImage_table"


class OrderModel(models.Model):
    """
    Model representing an order.

    Fields:
    - Order_id: AutoField, primary key.
    - Quantity: IntegerField.
    - User_id: ForeignKey linking to UserModel.
    - Variant_product_id: ForeignKey linking to VariantProductModel.
    - status: CharField with a default value of "Active".
    """
    Order_id = models.AutoField(primary_key=True, default=None)
    Quantity = models.IntegerField()
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    Variant_product_id = models.ForeignKey(VariantProductModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Active")

    class Meta:
        db_table = "Order_table"


class ReviewRatingModel(models.Model):
    """
    Model representing a review and rating.

    Fields:
    - Review_id: AutoField, primary key.
    - Review: CharField with a maximum length of 50 characters.
    - Rating: IntegerField.
    - Product_id: ForeignKey linking to ProductModel.
    - User_id: ForeignKey linking to UserModel.
    """
    Review_id = models.AutoField(primary_key=True, default=None)
    Review = models.CharField(max_length=50)
    Rating = models.IntegerField()
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Review

    class Meta:
        db_table = "Review_Rating_table"


class AddressModel(models.Model):
    """
    Model representing an address.

    Fields:
    - Address_id: AutoField, primary key.
    - House_Name: CharField with a maximum length of 50 characters.
    - House_Number: CharField with a maximum length of 50 characters.
    - Place: CharField with a maximum length of 50 characters.
    - Post: CharField with a maximum length of 50 characters.
    - Pincode: CharField with a maximum length of 50 characters.
    - Landmark: CharField with a maximum length of 50 characters.
    - User_id: ForeignKey linking to UserModel.
    """
    Address_id = models.AutoField(primary_key=True, default=None)
    House_Name = models.CharField(max_length=50)
    House_Number = models.CharField(max_length=50)
    Place = models.CharField(max_length=50)
    Post = models.CharField(max_length=50)
    Pincode = models.CharField(max_length=50)
    Landmark = models.CharField(max_length=50)
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.House_Name

    class Meta:
        db_table = "Address_table"


class CartModel(models.Model):
    """
    Model representing a shopping cart.

    Fields:
    - Cart_id: AutoField, primary key.
    - Quantity: IntegerField
    - Product_id: ForeignKey linking to ProductModel.
    - User_id: ForeignKey linking to UserModel.
    """
    Cart_id = models.AutoField(primary_key=True)
    Quantity = models.IntegerField()
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Cart_table"


class WishlistModel(models.Model):
    """
    Model representing a wishlist.

    Fields:
    - Wishlist_id: AutoField, primary key.
    - User_id: ForeignKey linking to UserModel.
    - Product_id: ForeignKey linking to ProductModel.
    """
    Wishlist_id = models.AutoField(primary_key=True)
    User_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "WishlistModel_table"
