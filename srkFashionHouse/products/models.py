from django.db import models
from django.contrib.auth.models import User
from django.db import models


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

    def str(self):
        return self.name

class RateProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.CharField(max_length=100, choices=[('1','1'),('2','2'),('3','3'), ('4','4') , ('5','5')])


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def str(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.product.price * self.quantity




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_orders")  # Unique related_name
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def str(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"



