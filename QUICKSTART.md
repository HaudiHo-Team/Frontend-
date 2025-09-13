# 🚀 Быстрый старт Frontend App

## Установка и запуск

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Запуск приложения

#### Вариант 1: Через скрипт запуска

```bash
python run.py
```

#### Вариант 2: Напрямую через Streamlit

```bash
streamlit run app.py
```

### 3. Открытие в браузере

Перейдите по адресу: **http://localhost:8501**

## 🏗️ Архитектура проекта

```
frontend/
├── app.py                    # 🎯 Главный файл приложения
├── run.py                    # 🚀 Скрипт запуска
├── requirements.txt          # 📦 Зависимости
├── .streamlit/              # ⚙️ Конфигурация Streamlit
├── src/                     # 📁 Исходный код
│   ├── components/          # 🧩 UI компоненты
│   ├── pages/              # 📄 Страницы
│   ├── utils/              # 🔧 Утилиты
│   └── config/             # ⚙️ Конфигурация
├── static/                 # 🎨 Статические файлы
├── tests/                  # 🧪 Тесты
└── docs/                   # 📚 Документация
```

## 📊 Функциональность

### 🏠 Главная страница

- Обзор системы и метрики
- Быстрые действия
- Уведомления

### 📊 Дашборд

- Интерактивные графики
- Фильтрация данных
- Экспорт результатов

### 📈 Аналитика

- Описательная статистика
- Корреляционный анализ
- Трендовый анализ
- Сегментация данных

### ⚙️ Настройки

- Профиль пользователя
- Настройки уведомлений
- Безопасность

## 🛠️ Разработка

### Добавление новой страницы

1. Создайте файл в `src/pages/`
2. Реализуйте функцию `render()`
3. Добавьте страницу в `app.py`

```python
# src/pages/new_page.py
def render():
    st.title("Новая страница")
    # Ваш код здесь
```

### Добавление нового компонента

1. Создайте файл в `src/components/`
2. Реализуйте функции компонента
3. Импортируйте в `__init__.py`

```python
# src/components/new_component.py
def render_new_widget():
    st.write("Новый виджет")
```

### Добавление новой утилиты

1. Создайте файл в `src/utils/`
2. Реализуйте класс или функции
3. Импортируйте в `__init__.py`

## 🔧 Конфигурация

### Настройки приложения

Измените файл `src/config/app_config.py`:

```python
config = AppConfig()
config.set('ui.theme', 'dark')
config.set('data.cache_ttl', 7200)
```

### Переменные окружения

Создайте файл `.env`:

```env
STREAMLIT_THEME=dark
STREAMLIT_LANGUAGE=en
CACHE_TTL=7200
```

## 🧪 Тестирование

### Запуск тестов

```bash
pytest tests/
```

### Покрытие кода

```bash
pytest --cov=src tests/
```

## 📦 Развертывание

### Docker

```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

### Heroku

```bash
# Создайте Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Развертывание
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

## 🐛 Решение проблем

### Ошибка импорта модулей

```bash
# Убедитесь, что вы в корневой директории проекта
cd /path/to/frontend

# Проверьте структуру
ls -la src/
```

### Ошибка зависимостей

```bash
# Переустановите зависимости
pip install -r requirements.txt --force-reinstall
```

### Проблемы с кэшем

```bash
# Очистите кэш Streamlit
streamlit cache clear
```

## 📚 Дополнительные ресурсы

- [Документация Streamlit](https://docs.streamlit.io/)
- [Архитектура проекта](docs/architecture.md)
- [API Reference](docs/api.md)
- [Руководство по развертыванию](docs/deployment.md)

## 🤝 Поддержка

- **Email**: support@frontendapp.com
- **GitHub Issues**: [Создать issue](https://github.com/frontendapp/issues)
- **Документация**: [docs.frontendapp.com](https://docs.frontendapp.com)

---

**Frontend App** - Современное решение для анализа данных с использованием Streamlit 🚀
