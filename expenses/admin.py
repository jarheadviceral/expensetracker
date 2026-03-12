from django.contrib import admin

from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'amount', 'date_created', 'username')
    list_filter = ('category', 'date_created')
    search_fields = ('item_name', 'category', 'username')
