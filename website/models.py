from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200, default='')
    prix = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField("date published")


class Materiel(models.Model):
    materiel = models.ForeignKey(Product, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
