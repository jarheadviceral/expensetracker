from django.db import models
import uuid


class Profile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=80)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Subscriptions', 'Subscriptions'),
        ('Shopping', 'Shopping'),
        ('Entertainment', 'Entertainment'),
        ('Utilities', 'Utilities'),
        ('School', 'School'),
        ('Other', 'Other'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    item_name = models.CharField(max_length=120)

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    date_created = models.DateField()

    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-date_created', '-id']

    def __str__(self):
        return f"{self.item_name} ({self.amount})"