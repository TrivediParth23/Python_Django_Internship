# Generated by Django 4.2.1 on 2023-06-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order_tick_marked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='place_order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='tick_marked',
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='item_json',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(max_length=100),
        ),
    ]
