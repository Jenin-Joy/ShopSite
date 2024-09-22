from django.db import models

# Create your models here.

class tbl_category(models.Model):
    category_name = models.CharField(max_length=30)

class tbl_brands(models.Model):
    brand_name = models.CharField(max_length=30)

class tbl_admregistration(models.Model):
    admregistration_name = models.CharField(max_length=30)
    admregistration_email = models.CharField(max_length=30)
    admregistration_password = models.CharField(max_length=30)

class tbl_subcategory(models.Model):
    subcategory_name = models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_shop(models.Model):
    shop_name = models.CharField(max_length=30)
    shop_email = models.CharField(max_length=30)
    shop_details = models.CharField(max_length=30)
    shop_password = models.CharField(max_length=30)
    shop_photo=models.FileField(upload_to='Assets/Shop/')

class tbl_product(models.Model):
    product_name = models.CharField(max_length=30)
    product_details = models.CharField(max_length=30)
    product_price = models.CharField(max_length=30)
    product_photo=models.FileField(upload_to='Assets/Product/')
    brand=models.ForeignKey(tbl_brands,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)

    