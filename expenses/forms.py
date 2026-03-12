from django import forms
from .models import Expense


class UsernameForm(forms.Form):
    username = forms.CharField(
        max_length=80,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your profile name',
                'class': 'form-control retro-input',
                'autocomplete': 'off',
            }
        ),
    )


class ExpenseForm(forms.ModelForm):

    date_created = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control retro-input'
            }
        )
    )

    class Meta:
        model = Expense
        fields = ['item_name', 'amount', 'date_created', 'category', 'notes']

        widgets = {

            'item_name': forms.TextInput(
                attrs={
                    'placeholder': 'What did you buy?',
                    'class': 'form-control retro-input'
                }
            ),

            'amount': forms.NumberInput(
                attrs={
                    'step': '0.01',
                    'min': '0',
                    'class': 'form-control retro-input'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-select retro-select'
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'rows': 2,
                    'placeholder': 'Optional note',
                    'class': 'form-control retro-input'
                }
            ),
        }