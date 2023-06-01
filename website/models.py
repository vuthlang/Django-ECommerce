from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.product_name


class Materiel(models.Model):
    materiel = models.ForeignKey(Product, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
