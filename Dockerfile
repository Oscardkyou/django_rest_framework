# Указываем базовый образ Python
FROM python:3.11

# Устанавливаем переменную окружения для уровня логирования FastAPI
ENV LOG_LEVEL=info

# Устанавливаем директорию приложения в контейнере
WORKDIR /app

# Копируем зависимости проекта
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы проекта в контейнер
COPY . .

# Запускаем сервер FastAPI при старте контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
