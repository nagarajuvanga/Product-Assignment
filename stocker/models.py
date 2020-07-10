from django.db import models

class Product(models.Model):
    product_no=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    product_quantity=models.IntegerField()
