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

    def _str_(self):
        return self.name