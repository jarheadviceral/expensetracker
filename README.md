# Retro Expense Tracker

A Django + SQLite expense tracker with a playful early-2000s web aesthetic inspired by Windows XP and MySpace profile pages.

## Features

- Username onboarding stored in session.
- Expense CRUD (create, edit, delete).
- Daily/weekly/monthly/yearly expense filtering.
- Insight cards (totals, top category, average daily, month-over-month change).
- Chart.js visualizations: category pie + monthly spend line chart.
- Retro UI with fixed blurred Bliss-style wallpaper background.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.
