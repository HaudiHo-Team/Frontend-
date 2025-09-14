# 🚀 Быстрый старт Frontend App

> **TL;DR**: Активируйте виртуальное окружение (`source venv/bin/activate`) и запустите `python run.py`. Откройте http://localhost:8501

## ✅ Быстрый чек-лист

- [ ] Python 3.8+ установлен
- [ ] Проект склонирован/скачан
- [ ] Виртуальное окружение создано (`make install`)
- [ ] Зависимости установлены
- [ ] Приложение запущено (`make run`)
- [ ] Браузер открыт на http://localhost:8501
- [ ] Интерфейс загружается без ошибок

> **💡 Если что-то не работает**: Используйте `make check` для диагностики или обратитесь к разделу "Решение проблем"

## 📋 Системные требования

- **Python**: 3.8+ (рекомендуется 3.9+)
- **ОС**: macOS, Linux, Windows
- **Память**: минимум 2GB RAM
- **Дисковое пространство**: 500MB для зависимостей

### Проверка системы

```bash
# Проверка версии Python
python3 --version

# Проверка доступной памяти (macOS/Linux)
free -h  # Linux
vm_stat  # macOS

# Проверка дискового пространства
df -h
```

### Установка Python (если не установлен)

#### macOS

```bash
# Через Homebrew (рекомендуется)
brew install python3

# Или скачайте с python.org
```

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### Windows

- Скачайте с [python.org](https://python.org)
- Или используйте [Chocolatey](https://chocolatey.org): `choco install python`
- Или используйте [Scoop](https://scoop.sh): `scoop install python`

## Установка и запуск

### 1. Создание и активация виртуального окружения

```bash
# Создание виртуального окружения (если еще не создано)
python3 -m venv venv

# Активация виртуального окружения
# На macOS/Linux:
source venv/bin/activate

# На Windows:
# venv\Scripts\activate
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Запуск приложения

#### Вариант 1: Через скрипт запуска (рекомендуется)

```bash
# Убедитесь, что виртуальное окружение активировано
source venv/bin/activate
python run.py
```

#### Вариант 2: Напрямую через Streamlit

```bash
# Убедитесь, что виртуальное окружение активировано
source venv/bin/activate
streamlit run app.py
```

#### Вариант 3: Одной командой

```bash
source venv/bin/activate && python run.py
```

#### Вариант 4: С дополнительными параметрами

```bash
# Запуск с отладкой
source venv/bin/activate
streamlit run app.py --logger.level debug

# Запуск на другом порту
source venv/bin/activate
streamlit run app.py --server.port 8502

# Запуск без браузера
source venv/bin/activate
streamlit run app.py --server.headless true
```

#### Вариант 5: Через Makefile (рекомендуется)

```bash
# Показать все доступные команды
make help

# Полная установка и запуск
make all

# Или пошагово:
make install  # Установка зависимостей
make run      # Запуск приложения
make dev      # Запуск в режиме разработки
make clean    # Очистка проекта
make status   # Проверка статуса
make check    # Проверка готовности к запуску
```

#### Вариант 6: Через скрипт запуска

```bash
# Простой скрипт для быстрого запуска
./start.sh
```

> **💡 Совет**: Makefile и start.sh уже созданы в проекте и содержат все необходимые команды с цветным выводом и проверками.

### 4. Открытие в браузере

Перейдите по адресу: **http://localhost:8501**

### 5. Проверка работоспособности

После запуска приложения вы должны увидеть:

1. **В терминале**:

   ```
   🚀 Запуск Frontend App...
   📱 Откройте браузер по адресу: http://localhost:8501
   ⏹️  Для остановки нажмите Ctrl+C
   --------------------------------------------------
   You can now view your Streamlit app in your browser.
   URL: http://localhost:8501
   ```

2. **В браузере**:

   - Загружается главная страница приложения
   - Отображается интерфейс без ошибок
   - Все компоненты работают корректно

3. **Проверка логов**:
   ```bash
   # Если есть ошибки, проверьте логи
   tail -f ~/.streamlit/logs/streamlit.log
   ```

## ⚡ Быстрые команды

### Полная настройка с нуля

```bash
# Клонирование и настройка проекта
git clone <repository-url>
cd frontend

# Вариант 1: Через Makefile
make all

# Вариант 2: Через скрипт
./start.sh
```

### Ежедневный запуск

```bash
# Через Makefile (рекомендуется)
make run

# Через скрипт
./start.sh

# Или вручную
source venv/bin/activate && python run.py
```

### Остановка приложения

```bash
# В терминале где запущено приложение
Ctrl + C
```

### Проверка статуса

```bash
# Через Makefile
make status   # Показать статус проекта
make check    # Проверить готовность к запуску

# Вручную
curl http://localhost:8501

# Или откройте браузер
open http://localhost:8501  # macOS
# xdg-open http://localhost:8501  # Linux
```

### Полезные команды Makefile

```bash
make help     # Показать все доступные команды
make install  # Установить зависимости
make run      # Запустить приложение
make dev      # Запуск в режиме разработки
make test     # Запустить тесты
make lint     # Проверить код
make format   # Форматировать код
make clean    # Очистить проект
make status   # Показать статус
make check    # Проверить готовность
make all      # Полная установка и запуск
```

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

### ❌ Ошибка "command not found: python"

**Проблема**: Команда `python` не найдена при запуске.

**Решение**:

```bash
# 1. Активируйте виртуальное окружение
source venv/bin/activate

# 2. Проверьте, что Python доступен
which python
# Должно показать: /path/to/frontend/venv/bin/python

# 3. Запустите приложение
python run.py
```

### ❌ Ошибка "Streamlit не установлен"

**Проблема**: Streamlit не найден в системе.

**Решение**:

```bash
# 1. Активируйте виртуальное окружение
source venv/bin/activate

# 2. Установите зависимости
pip install -r requirements.txt

# 3. Проверьте установку
streamlit --version
```

### ❌ Ошибка импорта модулей

**Проблема**: Модули из `src/` не импортируются.

**Решение**:

```bash
# Убедитесь, что вы в корневой директории проекта
cd /path/to/frontend

# Проверьте структуру
ls -la src/

# Убедитесь, что виртуальное окружение активировано
source venv/bin/activate
```

### ❌ Ошибка зависимостей

**Проблема**: Конфликты версий или отсутствующие пакеты.

**Решение**:

```bash
# 1. Активируйте виртуальное окружение
source venv/bin/activate

# 2. Обновите pip
pip install --upgrade pip

# 3. Переустановите зависимости
pip install -r requirements.txt --force-reinstall

# 4. Если проблемы продолжаются, создайте новое окружение
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ❌ Проблемы с кэшем

**Проблема**: Устаревший кэш Streamlit.

**Решение**:

```bash
# Очистите кэш Streamlit
streamlit cache clear

# Или удалите кэш вручную
rm -rf ~/.streamlit/cache/
```

### ❌ Порт 8501 занят

**Проблема**: Порт уже используется другим процессом.

**Решение**:

```bash
# 1. Найдите процесс, использующий порт
lsof -i :8501

# 2. Завершите процесс (замените PID на реальный)
kill -9 <PID>

# 3. Или запустите на другом порту
streamlit run app.py --server.port 8502
```

### ❌ Предупреждения конфигурации

**Проблема**: Предупреждения о недопустимых опциях конфигурации.

**Решение**:

```bash
# Установите watchdog для лучшей производительности
pip install watchdog

# Или игнорируйте предупреждения - они не критичны
```

### ❌ Проблемы на Windows

**Проблема**: Ошибки при активации виртуального окружения на Windows.

**Решение**:

```cmd
# Используйте правильный синтаксис для Windows
venv\Scripts\activate

# Или используйте PowerShell
venv\Scripts\Activate.ps1

# Если возникает ошибка выполнения скриптов:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Проблема**: Команда `make` не найдена на Windows.

**Решение**:

```cmd
# Установите Make через Chocolatey
choco install make

# Или используйте команды напрямую:
venv\Scripts\activate
python run.py
```

### 🔧 Диагностика проблем

```bash
# 1. Проверьте версию Python
python --version

# 2. Проверьте установленные пакеты
pip list

# 3. Проверьте переменные окружения
echo $VIRTUAL_ENV

# 4. Проверьте права доступа
ls -la venv/bin/python
```

## ❓ Часто задаваемые вопросы (FAQ)

### Q: Зачем нужно виртуальное окружение?

**A**: Виртуальное окружение изолирует зависимости проекта от системных пакетов Python, предотвращая конфликты версий и обеспечивая воспроизводимость окружения.

### Q: Можно ли запустить без виртуального окружения?

**A**: Технически да, но не рекомендуется. Это может привести к конфликтам зависимостей и проблемам с развертыванием.

### Q: Как обновить зависимости?

**A**:

```bash
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

### Q: Приложение не запускается, что делать?

**A**: Следуйте пошаговой диагностике:

1. Проверьте активацию виртуального окружения
2. Убедитесь, что все зависимости установлены
3. Проверьте логи ошибок
4. Обратитесь к разделу "Решение проблем"

### Q: Можно ли изменить порт?

**A**: Да, используйте параметр `--server.port`:

```bash
streamlit run app.py --server.port 8502
```

### Q: Как остановить приложение?

**A**: В терминале нажмите `Ctrl + C` или закройте терминал.

### Q: Где хранятся настройки Streamlit?

**A**: В директории `~/.streamlit/` (глобальные) или `.streamlit/` в проекте (локальные).

### Q: Как очистить кэш?

**A**:

```bash
streamlit cache clear
# или
rm -rf ~/.streamlit/cache/
```

### Q: Можно ли запустить в фоновом режиме?

**A**: Да, используйте `nohup` или `screen`:

```bash
nohup streamlit run app.py --server.headless true &
```

### Q: Как проверить, что приложение работает?

**A**:

```bash
curl http://localhost:8501
# Должен вернуть HTML-код страницы
```

### Q: Как ускорить загрузку приложения?

**A**:

```bash
# Установите watchdog для автоматической перезагрузки
pip install watchdog

# Используйте кэширование
streamlit run app.py --server.enableCORS false
```

### Q: Можно ли запустить на другом хосте?

**A**: Да, используйте параметр `--server.address`:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

### Q: Как настроить HTTPS?

**A**: Используйте параметры сертификата:

```bash
streamlit run app.py --server.sslCertFile cert.pem --server.sslKeyFile key.pem
```

## 🚀 Производительность и оптимизация

### Ускорение запуска

```bash
# Установите watchdog для быстрой перезагрузки
pip install watchdog

# Используйте предварительно скомпилированные пакеты
pip install --only-binary=all -r requirements.txt
```

### Оптимизация памяти

```bash
# Очистите кэш регулярно
streamlit cache clear

# Используйте профилирование памяти
pip install memory-profiler
```

### Настройка для продакшена

```bash
# Запуск в headless режиме
streamlit run app.py --server.headless true --server.enableCORS false

# Настройка логирования
streamlit run app.py --logger.level warning
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
