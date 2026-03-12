import json
from datetime import date, timedelta
from decimal import Decimal

from django.contrib import messages
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import ExpenseForm, UsernameForm
from .models import Expense


def username_entry(request):
    saved_profiles = (
        Expense.objects.exclude(username='')
        .values_list('username', flat=True)
        .distinct()
        .order_by('username')
    )

    if request.method == 'POST':
        form = UsernameForm(request.POST)
        if form.is_valid():
            request.session['username'] = form.cleaned_data['username']
            return redirect('dashboard')
    else:
        form = UsernameForm(initial={'username': request.session.get('username', '')})
    return render(
        request,
        'expenses/username.html',
        {
            'form': form,
            'saved_profiles': saved_profiles,
            'active_username': request.session.get('username'),
        },
    )


def switch_profile(request):
    if request.method == 'POST':
        request.session.pop('username', None)
        messages.info(request, 'Profile saved. You can switch or create another account anytime.')
    return redirect('username-entry')


def _date_filter(range_filter: str):
    today = timezone.localdate()
    if range_filter == 'daily':
        start = today
    elif range_filter == 'weekly':
        start = today - timedelta(days=today.weekday())
    elif range_filter == 'yearly':
        start = date(today.year, 1, 1)
    else:
        range_filter = 'monthly'
        start = date(today.year, today.month, 1)
    return range_filter, start, today


def dashboard(request):
    username = request.session.get('username')
    if not username:
        return redirect('username-entry')

    range_filter = request.GET.get('range', 'monthly')
    range_filter, start_date, end_date = _date_filter(range_filter)
    scoped_expenses = Expense.objects.filter(username=username, date_created__range=(start_date, end_date))

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.username = username
            expense.save()
            messages.success(request, 'Expense added to your retro ledger!')
            return redirect('dashboard')
    else:
        form = ExpenseForm(initial={'date_created': timezone.localdate()})

    total_spending = scoped_expenses.aggregate(total=Sum('amount'))['total'] or Decimal('0')

    category_totals_qs = scoped_expenses.values('category').annotate(total=Sum('amount')).order_by('-total')
    category_totals = [
        {'category': row['category'].title(), 'total': float(row['total'])}
        for row in category_totals_qs
    ]
    top_category = category_totals[0]['category'] if category_totals else 'N/A'

    days_count = max((end_date - start_date).days + 1, 1)
    average_daily = total_spending / Decimal(days_count)

    first_of_month = date(end_date.year, end_date.month, 1)
    prev_month_end = first_of_month - timedelta(days=1)
    prev_month_start = date(prev_month_end.year, prev_month_end.month, 1)
    current_month_total = Expense.objects.filter(
        username=username,
        date_created__range=(first_of_month, end_date),
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0')
    prev_month_total = Expense.objects.filter(
        username=username,
        date_created__range=(prev_month_start, prev_month_end),
    ).aggregate(total=Sum('amount'))['total'] or Decimal('0')
    spending_change = current_month_total - prev_month_total

    monthly_data_qs = (
        Expense.objects.filter(username=username)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )
    monthly_data = [
        {'month': row['month'].strftime('%b %Y'), 'total': float(row['total'])}
        for row in monthly_data_qs
    ]

    all_expenses = Expense.objects.filter(username=username)
    stats = {
        'total_entries': all_expenses.count(),
        'current_month_total': current_month_total,
    }

    context = {
        'username': username,
        'form': form,
        'expenses': scoped_expenses,
        'range_filter': range_filter,
        'total_spending': total_spending,
        'top_category': top_category,
        'average_daily': average_daily,
        'spending_change': spending_change,
        'category_totals_json': json.dumps(category_totals),
        'monthly_data_json': json.dumps(monthly_data),
        'stats': stats,
    }
    return render(request, 'expenses/dashboard.html', context)


def expense_edit(request, expense_id):
    username = request.session.get('username')
    if not username:
        return redirect('username-entry')

    expense = get_object_or_404(Expense, id=expense_id, username=username)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated!')
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/expense_edit.html', {'form': form, 'expense': expense})


def expense_delete(request, expense_id):
    username = request.session.get('username')
    if not username:
        return redirect('username-entry')

    expense = get_object_or_404(Expense, id=expense_id, username=username)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted from timeline.')
    return redirect('dashboard')
