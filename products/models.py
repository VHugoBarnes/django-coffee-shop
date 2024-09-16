from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="products/photos", null=True, blank=True)

    def __str__(self):
        return self.name
