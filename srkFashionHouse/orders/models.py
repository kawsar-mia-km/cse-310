
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomOrder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    design_description = models.TextField()
    design_image = models.ImageField(upload_to='design_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")  # Unique related_name
    customer = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

