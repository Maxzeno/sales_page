from django.db import models
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    link = models.URLField(max_length=1024, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    slashed_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sold = models.IntegerField(default=0, blank=True, null=True)
    priority = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.name


class Script(models.Model):
    tag = models.CharField(max_length=2000)