from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        default=0
    )
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.product_name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
