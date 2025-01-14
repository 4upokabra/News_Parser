FROM python:3.11 as builder

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Удаляем файл requirements.txt для уменьшения размера образа
RUN rm requirements.txt

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . .

# Запускаем скрипт для сборки и установки зависимостей
CMD ["python", "main.py"]
