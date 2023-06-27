# Используйте базовый образ Python
FROM python:3.9

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка GDAL
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin

# Установка рабочей директории внутри контейнера
WORKDIR /code

# Установка зависимостей
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода проекта внутрь контейнера
COPY . /code/

# Запуск сервера Django
CMD python manage.py runserver 0.0.0.0:8000
