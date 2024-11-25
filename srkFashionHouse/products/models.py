from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='products',null=True, blank=True)
    description = models.TextField()
    def __str__(self):
        return self.name