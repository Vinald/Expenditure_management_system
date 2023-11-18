from django.db import models


CATEGORY = (
    ('Food', 'Food'),
    ('Clothes', 'Clothes'),
    ('Stationary', 'Stationary'),
    ('Others', 'Others'),
)


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name