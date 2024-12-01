from django.db import models

# Create your models here.
class CustomOrder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    design_description = models.TextField()
    design_image = models.ImageField(upload_to='design_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order:
    pass