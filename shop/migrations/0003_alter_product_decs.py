# Generated by Django 4.2.1 on 2023-06-06 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='decs',
            field=models.CharField(max_length=5000),
        ),
    ]
