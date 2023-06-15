import os
from celery import Celery

# Установка переменной окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_service.settings')

app = Celery('email_service')

# Загрузка конфигурации из файла settings.py проекта Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из приложений Django
app.autodiscover_tasks()
