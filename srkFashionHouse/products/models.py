from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    description = models.TextField()

    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('children', 'Children'),
    ]

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='women',
    )

    def _str_(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.product.price * self.quantity