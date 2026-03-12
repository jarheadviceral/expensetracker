from django.db import models


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('subscriptions', 'Subscriptions'),
        ('shopping', 'Shopping'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('school', 'School'),
        ('other', 'Other'),
    ]

    username = models.CharField(max_length=80, blank=True)
    item_name = models.CharField(max_length=120)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date_created', '-id']

    def __str__(self):
        return f'{self.item_name} ({self.amount})'
