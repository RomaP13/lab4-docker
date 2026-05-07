# ЛР №4 - Контейнеризація методу Ньютона
FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо код
COPY main.py .

# Команда запуску
CMD ["python3", "main.py"]
