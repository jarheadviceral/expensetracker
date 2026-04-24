import os
from django.core.wsgi import get_wsgi_application
from mangum import Mangum

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "retro_expense_tracker.settings")

app = get_wsgi_application()
handler = Mangum(app)