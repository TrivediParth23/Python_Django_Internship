# Generated by Django 4.2.1 on 2023-06-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_orders_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='zip_code',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='item_json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
