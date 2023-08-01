from django.db import models

class Item(models.Model):
    Number=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=20)
    price=models.IntegerField()
    