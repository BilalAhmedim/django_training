from django.db import models


# Create your models here.
class FeaturedApp(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
