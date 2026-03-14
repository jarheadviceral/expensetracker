from django.urls import path

from . import views

urlpatterns = [
    path('', views.username_view, name='username-entry'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expense/<int:expense_id>/edit/', views.expense_edit, name='expense-edit'),
    path('expense/<int:expense_id>/delete/', views.expense_delete, name='expense-delete'),
]
