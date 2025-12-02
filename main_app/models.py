from django.db import models
from cloudinary.models import CloudinaryField


class ManService(models.Model):
    image = models.ImageField(null=True, blank=True)
    service_type = models.CharField(blank=True, null=True, max_length=255)
    price = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_type


class WomanService(models.Model):
    image = models.ImageField(null=True, blank=True)
    service_type = models.CharField(blank=True, null=True, max_length=255)
    price = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_type


class KidService(models.Model):
    image = models.ImageField(null=True, blank=True)
    service_type = models.CharField(blank=True, null=True, max_length=255)
    price = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_type
