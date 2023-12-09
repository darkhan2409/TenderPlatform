from django.db import models
from category_app.models import Category
from status_app.models import Status

TYPE_CHOICES = [
    ('Open Tender', 'Open Tender'),
    ('Close Tender', 'Close Tender'),
    ('Auction', 'Auction'),
    ('Negotiation', 'Negotiation')
]


class Purchase(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    description = models.TextField()
    budget = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    delivery = models.TextField()
    terms = models.DateField()
    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return str(self.title)

