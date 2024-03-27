from django.db import models
from UserApp import *


class AdminModel(models.Model):
    """
    Model representing an administrator user.

    Fields:
        Admin_id (int): The unique identifier for the administrator.
        Admin_name (str): The name of the administrator.
        phone_number (str): The phone number of the administrator.
        email (str): The email address of the administrator.
        password (str): The password of the administrator.
    """

    Admin_id = models.IntegerField(primary_key=True, default=None)
    Admin_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "Admin_table"


class MainCategoryModel(models.Model):
    """
    Model representing main categories for products.

    Fields:
        Main_category_id (int): The unique identifier for the main category.
        Main_category (str): The name of the main category.
    """

    Main_category_id = models.IntegerField(primary_key=True, default=None)
    Main_category = models.CharField(max_length=50)

    def __str__(self):
        return self.Main_category

    class Meta:
        db_table = "MainCategory_table"


class SubCategoryModel(models.Model):
    """
    Model representing sub-categories for products.

    Fields:
        Sub_category_id (int): The unique identifier for the sub-category.
        Sub_category (str): The name of the sub-category.
        Main_category_id (MainCategoryModel): The main category to which the sub-category belongs (foreign key).
    """

    Sub_category_id = models.IntegerField(primary_key=True, default=None)
    Sub_category = models.CharField(max_length=50)
    Main_category_id = models.ForeignKey(MainCategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Sub_category

    class Meta:
        db_table = "SubCategory_table"


class SubSubCategoryModel(models.Model):
    """
    Model representing sub-sub-categories for products.

    Fields:
        Sub_sub_category_id (int): The unique identifier for the sub-sub-category.
        Sub_sub_category (str): The name of the sub-sub-category.
        Sub_category_id (SubCategoryModel): The sub-category to which the sub-sub-category belongs (foreign key).
    """

    Sub_sub_category_id = models.IntegerField(primary_key=True, default=None)
    Sub_sub_category = models.CharField(max_length=50)
    Sub_category_id = models.ForeignKey(SubCategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Sub_sub_category

    class Meta:
        db_table = "Sub_sub_category_table"


class BrandModel(models.Model):
    """
    Model representing product brands.

    Fields:
        Brand_id (int): The unique identifier for the brand.
        image (ImageField): The image representing the brand.
        Brand_name (str): The name of the brand.
    """

    Brand_id = models.IntegerField(primary_key=True, default=None)
    image = models.ImageField(upload_to='images/')
    Brand_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Brand_name

    class Meta:
        db_table = "Brand_table"


class ProductModel(models.Model):
    """
    Model representing products.

    Fields:
        Product_id (int): The unique identifier for the product.
        Product_title (str): The title of the product.
        Product_description (str): The description of the product.
        Quantity (int): The quantity of the product available.
        Price (int): The price of the product.
        status (str): The status of the product (e.g., Active, Inactive).
        Main_category_id (MainCategoryModel): The main category to which the product belongs (foreign key).
        Brand_id (BrandModel): The brand of the product (foreign key).
    """

    Product_id = models.AutoField(primary_key=True, default=None)
    Product_title = models.CharField(max_length=50)
    Product_description = models.CharField(max_length=50)
    Quantity = models.IntegerField(null=True)
    Price = models.IntegerField()
    status = models.CharField(max_length=50, default="Active")
    Main_category_id = models.ForeignKey(MainCategoryModel, on_delete=models.CASCADE, null=True)
    Brand_id = models.ForeignKey(BrandModel, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.Product_title

    class Meta:
        db_table = "Product_table"


class ProductImageModel(models.Model):
    """
    Model representing images associated with products.

    Fields:
        image_id (int): The unique identifier for the product image.
        images (ImageField): The image associated with the product.
        Product_id (ProductModel): The product to which the image belongs (foreign key).
    """

    image_id = models.IntegerField(primary_key=True, default=None)
    images = models.ImageField(upload_to='images/')
    Product_id = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE)

    class Meta:
        db_table = "Product_image_table"


class VariantProductModel(models.Model):
    """
    Model representing variant products.

    Fields:
        Variant_product_id (int): The unique identifier for the variant product.
        Variant_product_name (str): The name of the variant product.
        Size (int): The size of the variant product.
        Quantity (str): The quantity of the variant product.
        Color (str): The color of the variant product.
        Occasion (str): The occasion for which the variant product is suitable.
        Neck (str): The neck type of the variant product.
        Bottom_Fabric (str): The fabric used for the bottom part of the variant product.
        Top_type (str): The type of the top part of the variant product.
        Sleeve_Length (str): The length of the sleeves of the variant product.
        Top_Fabric (str): The fabric used for the top part of the variant product.
        Bottom_Type (str): The type of the bottom part of the variant product.
        Bottom_Pattern (str): The pattern of the bottom part of the variant product.
        price (str): The price of the variant product.
        Product_id (ProductModel): The product to which the variant product belongs (foreign key).
    """

    Variant_product_id = models.IntegerField(primary_key=True, default=None)
    Variant_product_name = models.CharField(max_length=50)
    Size = models.IntegerField()
    Quantity = models.CharField(max_length=50, null=True)
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

    def __str__(self):
        return self.Variant_product_name

    class Meta:
        db_table = "Variant_Product_table"


class OfferEventModel(models.Model):
    """
    Model representing special offers or events.

    Fields:
        Offer_id (int): The unique identifier for the offer/event.
        Offer_Name (str): The name of the offer/event.
        Start_Date (DateField): The start date of the offer/event.
        End_Date (DateField): The end date of the offer/event.
        images (ImageField): The image associated with the offer/event.
    """

    Offer_id = models.IntegerField(primary_key=True, default=None)
    Offer_Name = models.CharField(max_length=50)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    images = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.Offer_Name

    class Meta:
        db_table = "Offer_Event_table"


class OfferModel(models.Model):
    """
    Model representing offers.

    Fields:
        Event_id (int): The unique identifier for the offer.
        Discount (int): The discount percentage offered.
        Offer_id (OfferEventModel): The offer/event to which the offer belongs (foreign key).
        Product_id (ProductModel): The product to which the offer applies (foreign key).
    """

    Event_id = models.IntegerField(primary_key=True, default=None)
    Discount = models.IntegerField()
    Offer_id = models.ForeignKey(OfferEventModel, on_delete=models.CASCADE)
    Product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "Offer_table"


class DistrictModel(models.Model):
    """
    Model representing districts.

    Fields:
        District_id (int): The unique identifier for the district.
        District_Name (str): The name of the district.
    """

    District_id = models.IntegerField(primary_key=True, default=None)
    District_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.District_Name

    class Meta:
        db_table = "District_table"


class CityModel(models.Model):
    """
    Model representing cities.

    Fields:
        City_id (int): The unique identifier for the city.
        City_Name (str): The name of the city.
        District_id (DistrictModel): The district to which the city belongs (foreign key).
    """

    City_id = models.IntegerField(primary_key=True, default=None)
    City_Name = models.CharField(max_length=50)
    District_id = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.City_Name

    class Meta:
        db_table = "City_table"
