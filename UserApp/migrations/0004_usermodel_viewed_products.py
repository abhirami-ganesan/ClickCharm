# Generated by Django 5.0.2 on 2024-03-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0004_offereventmodel_images'),
        ('UserApp', '0003_alter_cartmodel_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='viewed_products',
            field=models.ManyToManyField(blank=True, related_name='viewed_by', to='AdminApp.productmodel'),
        ),
    ]