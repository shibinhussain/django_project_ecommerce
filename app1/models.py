from django.db import models



# Create your models here.
class login_tb(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    class Meta:
        db_table="login_tb"

class createaccount(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    class Meta:
        db_table="createaccount"


class product_details(models.Model):
    productname=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField()
    offer=models.CharField(max_length=50)
    item=models.CharField(max_length=50)
    class Meta:
        db_table="product_details"

class seller_details(models.Model):
    sellerid = models.CharField(max_length=50)
    sellername = models.CharField(max_length=50)
    age = models.IntegerField()
    exp = models.IntegerField()
    sal = models.IntegerField()
    class Meta:
        db_table="seller_details"

class order_details(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    productname=models.CharField(max_length=50)
    price=models.IntegerField()
    class Meta:
        db_table="order_details"
