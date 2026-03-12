from datetime import date

from django.test import Client, TestCase
from django.urls import reverse

from .models import Expense


class DashboardFlowTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_username_redirect_and_create_expense(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

        self.client.post(reverse('username-entry'), {'username': 'Jared'})
        response = self.client.post(
            reverse('dashboard'),
            {
                'item_name': 'Pizza',
                'amount': '12.50',
                'date_created': date.today().isoformat(),
                'category': 'food',
                'notes': 'Friday dinner',
            },
            follow=True,
        )
        self.assertContains(response, 'Expense added to your retro ledger!')
        self.assertEqual(Expense.objects.count(), 1)
