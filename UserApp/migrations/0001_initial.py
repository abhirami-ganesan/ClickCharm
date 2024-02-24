# Generated by Django 5.0.2 on 2024-02-18 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('User_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=50)),
                ('Phone_Number', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('status', models.CharField(default='Active', max_length=50)),
            ],
            options={
                'db_table': 'User_table',
            },
        ),
        migrations.CreateModel(
            name='UserImageModel',
            fields=[
                ('Image_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Image', models.ImageField(upload_to='image')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'UserImage_table',
            },
        ),
        migrations.CreateModel(
            name='ReviewRatingModel',
            fields=[
                ('Review_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Review', models.CharField(max_length=50)),
                ('Rating', models.IntegerField()),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'Review_Rating_table',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('Order_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Quantity', models.IntegerField()),
                ('status', models.CharField(default='Active', max_length=50)),
                ('Variant_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.variantproductmodel')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'Order_table',
            },
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('Cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.CharField(max_length=50)),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.productmodel')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'Cart_table',
            },
        ),
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('Address_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('House_Name', models.CharField(max_length=50)),
                ('House_Number', models.CharField(max_length=50)),
                ('Place', models.CharField(max_length=50)),
                ('Post', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=50)),
                ('Landmark', models.CharField(max_length=50)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'Address_table',
            },
        ),
        migrations.CreateModel(
            name='WishlistModel',
            fields=[
                ('Wishlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.productmodel')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.usermodel')),
            ],
            options={
                'db_table': 'WishlistModel_table',
            },
        ),
    ]