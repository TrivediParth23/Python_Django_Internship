from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=256)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    decs = models.CharField(max_length=5000)
    pub_date =models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

class contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    email = models.CharField(max_length=50,default="")
    address1 = models.CharField(max_length=50,default="")
    address2 = models.CharField(max_length=50,default="")
    city = models.CharField(max_length=50,default="")
    state = models.CharField(max_length=50,default="")
    query = models.CharField(max_length=500,default="")
    tick = models.CharField(max_length=10,default="")

class order(models.Model):
    order_id = models.AutoField(primary_key=True)    
    item_json = models.CharField(max_length=5000,default="")
    name = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    city = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=100,default="")
    zip_code = models.CharField(max_length=100,default="")
    mobile_number = models.CharField(max_length=100,default="")
    tick_marked = models.CharField(max_length=100,default="")


