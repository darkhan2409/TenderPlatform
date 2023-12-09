from django.db import models
from purchase_app.models import Purchase


class Company(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    founders = models.TextField()
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    insta_link = models.TextField()

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.title

