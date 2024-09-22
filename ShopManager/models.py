from django.db import models
from Admin.models import *

# Create your models here.
class tbl_stock(models.Model):
    vendor_name=models.CharField(max_length=30)
    stock_quantity=models.CharField(max_length=30)
    product_id=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    stock_datetime=models.DateTimeField(auto_now_add=True)
    shop_id=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
class tbl_customer(models.Model):
    customer_name=models.CharField(max_length=30)
    customer_contact=models.CharField(max_length=30)

class tbl_purchase(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_status = models.IntegerField(default=0)
    customer = models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    shop = models.ForeignKey(tbl_shop, on_delete=models.CASCADE)

class tbl_items(models.Model):
    item_price=models.IntegerField()
    item_qty = models.IntegerField()
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(tbl_purchase, on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    customer = models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    purchase = models.ForeignKey(tbl_purchase, on_delete=models.CASCADE)
    quality = models.CharField(max_length=30)
    usability = models.CharField(max_length=30)
    price = models.CharField(max_length=30)