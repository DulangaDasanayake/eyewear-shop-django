from django.db import models

# Create your models here.


class Product(models.Model):
    STOCK_CHOICES = (
        ('available', 'AVAILABLE'),
        ('out_of_stock', 'OUT_OF_STOCK')
    )
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/products')
    status = models.CharField(choices=STOCK_CHOICES, max_length=20)

    def __str__(self):
        return self.name