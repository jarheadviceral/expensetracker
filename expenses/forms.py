from django import forms

from .models import Expense


class UsernameForm(forms.Form):
    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'placeholder': 'Enter your profile name'}))


class ExpenseForm(forms.ModelForm):
    date_created = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ['item_name', 'amount', 'date_created', 'category', 'notes']
        widgets = {
            'item_name': forms.TextInput(attrs={'placeholder': 'What did you buy?'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'category': forms.Select(),
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Optional note'}),
        }
