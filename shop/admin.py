from django.contrib import admin

# Register your models here.
from .models import product, contact , order

# admin.site.register(product) old registrations technique

@admin.register(contact)
class contactModelAdmin(admin.ModelAdmin):
    list_display = ['name','msg_id','email']

@admin.register(product)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['product_name','id','price']

@admin.register(order)
class orderModelAdmin(admin.ModelAdmin):
    list_display = ['name','order_id','email']
