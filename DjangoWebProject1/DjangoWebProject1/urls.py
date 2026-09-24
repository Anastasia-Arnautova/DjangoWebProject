from django.contrib import admin
from django.urls import path
from MyApp1.views import async_view  # Імпортуємо нашу асинхронну функцію

urlpatterns = [
    path('admin/', admin.site.urls),
    path('async-tasks/', async_view, name='async_tasks'),  # Додаємо URL для перегляду результатів
    path('', async_view)
]
