# 🚀 Команды Frontend App

## Быстрый старт

```bash
# Вариант 1: Через Makefile
make all

# Вариант 2: Через скрипт
./start.sh

# Или пошагово:
make install  # Установка зависимостей
make run      # Запуск приложения
```

## Основные команды

```bash
make help     # Показать все команды
make status   # Статус проекта
make check    # Проверка готовности
make run      # Запуск приложения
make dev      # Режим разработки
make test     # Запуск тестов
make clean    # Очистка проекта
```

## Ручной запуск

```bash
# Активация окружения
source venv/bin/activate

# Запуск приложения
python run.py

# Или напрямую через Streamlit
streamlit run app.py
```

## Диагностика

```bash
# Проверка статуса
make status

# Проверка готовности
make check

# Проверка порта
lsof -i :8501

# Проверка приложения
curl http://localhost:8501
```

## Разработка

```bash
# Форматирование кода
make format

# Проверка кода
make lint

# Запуск тестов
make test

# Очистка
make clean
```

## Полезные ссылки

- [QUICKSTART.md](QUICKSTART.md) - Подробное руководство
- [README.md](README.md) - Основная документация
- http://localhost:8501 - Приложение
