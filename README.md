# Frontend App - Streamlit Architecture

## 🚀 Описание

Современное веб-приложение на базе Streamlit с модульной архитектурой, предназначенное для анализа данных, визуализации и управления информацией.

## 📁 Архитектура проекта

```
frontend/
├── app.py                          # Главный файл приложения
├── requirements.txt                 # Зависимости Python
├── README.md                       # Документация
├── src/                           # Исходный код
│   ├── components/                # Переиспользуемые UI компоненты
│   │   ├── __init__.py
│   │   ├── header.py              # Заголовки и навигация
│   │   ├── cards.py               # Карточки и метрики
│   │   ├── charts.py              # Графики и визуализация
│   │   ├── tables.py              # Таблицы и данные
│   │   ├── forms.py               # Формы и ввод данных
│   │   └── filters.py             # Фильтры и селекторы
│   ├── pages/                     # Страницы приложения
│   │   ├── __init__.py
│   │   ├── home.py                # Главная страница
│   │   ├── dashboard.py           # Дашборд
│   │   ├── analytics.py           # Аналитика
│   │   └── settings.py            # Настройки
│   ├── utils/                     # Утилиты и вспомогательные функции
│   │   ├── __init__.py
│   │   ├── session_state.py       # Управление состоянием сессии
│   │   ├── data_loader.py         # Загрузка и обработка данных
│   │   ├── analytics.py           # Аналитические функции
│   │   ├── validators.py          # Валидация данных
│   │   └── helpers.py             # Вспомогательные функции
│   └── config/                    # Конфигурация
│       ├── __init__.py
│       └── app_config.py          # Настройки приложения
├── static/                        # Статические файлы
│   ├── css/                       # Стили CSS
│   ├── js/                        # JavaScript файлы
│   └── images/                    # Изображения
├── tests/                         # Тесты
└── docs/                          # Документация
```

## 🏗️ Архитектурные принципы

### 1. Модульность

- **Компоненты**: Переиспользуемые UI элементы
- **Страницы**: Логически разделенные разделы приложения
- **Утилиты**: Общие функции и классы
- **Конфигурация**: Централизованные настройки

### 2. Разделение ответственности

- **UI Layer**: Компоненты и страницы
- **Business Logic**: Утилиты и аналитика
- **Data Layer**: Загрузка и обработка данных
- **Configuration**: Настройки и конфигурация

### 3. Масштабируемость

- Легкое добавление новых страниц
- Расширяемая система компонентов
- Гибкая конфигурация
- Кэширование данных

## 🚀 Быстрый старт

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск приложения

```bash
streamlit run app.py
```

### Доступ к приложению

Откройте браузер и перейдите по адресу: `http://localhost:8501`

## 📊 Функциональность

### Главная страница

- Обзор системы
- Ключевые метрики
- Быстрые действия
- Уведомления

### Дашборд

- Интерактивные графики
- Фильтрация данных
- Экспорт результатов
- Детальная аналитика

### Аналитика

- Описательная статистика
- Корреляционный анализ
- Трендовый анализ
- Сегментация данных

### Настройки

- Профиль пользователя
- Настройки уведомлений
- Безопасность
- Конфигурация приложения

## 🛠️ Компоненты

### Header Components

- `render_page_header()` - Заголовок страницы
- `render_breadcrumb()` - Навигационные крошки
- `render_status_bar()` - Статусная строка

### Card Components

- `render_metrics_cards()` - Карточки метрик
- `render_info_card()` - Информационные карточки
- `render_feature_card()` - Карточки функций

### Chart Components

- `render_activity_chart()` - График активности
- `render_sales_trend_chart()` - Тренды продаж
- `render_category_pie_chart()` - Круговая диаграмма
- `render_correlation_heatmap()` - Тепловая карта корреляций

### Table Components

- `render_data_table()` - Таблица данных
- `render_editable_table()` - Редактируемая таблица
- `render_filterable_table()` - Фильтруемая таблица

### Form Components

- `render_login_form()` - Форма входа
- `render_contact_form()` - Форма обратной связи
- `render_data_entry_form()` - Форма ввода данных

## 🔧 Конфигурация

### Основные настройки

```python
# app.py
st.set_page_config(
    page_title="Frontend App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

### Конфигурация приложения

```python
# src/config/app_config.py
config = AppConfig()
config.get('ui.theme')  # 'light'
config.get('data.cache_ttl')  # 3600
```

## 📈 Аналитика

### Поддерживаемые типы анализа

- **Описательная статистика**: Средние, медианы, стандартные отклонения
- **Корреляционный анализ**: Пирсон, Спирмен, Кендалл
- **Трендовый анализ**: Временные ряды, прогнозирование
- **Сегментация**: K-means кластеризация

### Метрики

- Базовые метрики данных
- Бизнес-метрики
- Статистические показатели
- Обнаружение выбросов

## 🔒 Безопасность

### Аутентификация

- Простая система входа
- Управление сессиями
- Таймаут сессии

### Валидация данных

- Проверка типов данных
- Валидация форм
- Санитизация входных данных

## 🧪 Тестирование

### Запуск тестов

```bash
pytest tests/
```

### Покрытие кода

```bash
pytest --cov=src tests/
```

## 📝 Разработка

### Добавление новой страницы

1. Создайте файл в `src/pages/`
2. Реализуйте функцию `render()`
3. Добавьте страницу в `app.py`

### Добавление нового компонента

1. Создайте файл в `src/components/`
2. Реализуйте функции компонента
3. Импортируйте в `__init__.py`

### Добавление новой утилиты

1. Создайте файл в `src/utils/`
2. Реализуйте класс или функции
3. Импортируйте в `__init__.py`

## 🚀 Развертывание

### Локальное развертывание

```bash
streamlit run app.py --server.port 8501
```

### Docker (опционально)

```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 📚 Документация

### API Reference

- [Components API](docs/components.md)
- [Utils API](docs/utils.md)
- [Configuration API](docs/config.md)

### Руководства

- [Getting Started](docs/getting-started.md)
- [Architecture Guide](docs/architecture.md)
- [Deployment Guide](docs/deployment.md)

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для функции
3. Внесите изменения
4. Добавьте тесты
5. Создайте Pull Request

## 📄 Лицензия

MIT License - см. файл [LICENSE](LICENSE) для деталей.

## 👥 Команда

- **Разработка**: Development Team
- **Дизайн**: UI/UX Team
- **Аналитика**: Data Science Team

## 📞 Поддержка

- **Email**: support@frontendapp.com
- **Документация**: [docs.frontendapp.com](https://docs.frontendapp.com)
- **Issues**: [GitHub Issues](https://github.com/frontendapp/issues)

---

**Frontend App** - Современное решение для анализа данных с использованием Streamlit 🚀
