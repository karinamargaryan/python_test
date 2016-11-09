from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    price=models.IntegerField()
    status=models.IntegerField()
    weight=models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
