from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=80)),
                ('item_name', models.CharField(max_length=120)),
                ('category', models.CharField(choices=[('food', 'Food'), ('transport', 'Transport'), ('subscriptions', 'Subscriptions'), ('shopping', 'Shopping'), ('entertainment', 'Entertainment'), ('utilities', 'Utilities'), ('other', 'Other')], max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateField()),
                ('notes', models.TextField(blank=True)),
            ],
            options={'ordering': ['-date_created', '-id']},
        ),
    ]
