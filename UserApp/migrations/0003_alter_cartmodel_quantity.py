# Generated by Django 5.0.2 on 2024-03-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_reviewratingmodel_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='Quantity',
            field=models.IntegerField(),
        ),
    ]
