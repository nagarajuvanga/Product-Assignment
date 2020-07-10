from django.db import models

class Stocker(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    contact=models.IntegerField(unique=True)
    password=models.CharField(max_length=50)

