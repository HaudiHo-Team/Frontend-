.PHONY: install run dev clean help

# Цвета для вывода
GREEN=\033[0;32m
YELLOW=\033[1;33m
RED=\033[0;31m
NC=\033[0m # No Color

help: ## Показать справку
	@echo "$(GREEN)Frontend App - Команды управления$(NC)"
	@echo ""
	@echo "$(YELLOW)Доступные команды:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}'

install: ## Установить зависимости
	@echo "$(GREEN)🔧 Создание виртуального окружения...$(NC)"
	python3 -m venv venv
	@echo "$(GREEN)📦 Установка зависимостей...$(NC)"
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt
	@echo "$(GREEN)✅ Установка завершена!$(NC)"

run: ## Запустить приложение
	@echo "$(GREEN)🚀 Запуск Frontend App...$(NC)"
	. venv/bin/activate && python run.py

dev: ## Запуск в режиме разработки
	@echo "$(GREEN)🔧 Запуск в режиме разработки...$(NC)"
	. venv/bin/activate && streamlit run app.py --logger.level debug

test: ## Запустить тесты
	@echo "$(GREEN)🧪 Запуск тестов...$(NC)"
	. venv/bin/activate && pytest tests/ -v

lint: ## Проверка кода
	@echo "$(GREEN)🔍 Проверка кода...$(NC)"
	. venv/bin/activate && flake8 src/
	. venv/bin/activate && black --check src/

format: ## Форматирование кода
	@echo "$(GREEN)✨ Форматирование кода...$(NC)"
	. venv/bin/activate && black src/

clean: ## Очистка проекта
	@echo "$(YELLOW)🧹 Очистка проекта...$(NC)"
	rm -rf venv/
	rm -rf __pycache__/
	rm -rf .streamlit/cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "$(GREEN)✅ Очистка завершена!$(NC)"

status: ## Проверить статус
	@echo "$(GREEN)📊 Статус проекта:$(NC)"
	@echo "Python: $$(python3 --version 2>/dev/null || echo 'Не установлен')"
	@echo "Виртуальное окружение: $$(if [ -d venv ]; then echo '✅ Создано'; else echo '❌ Не создано'; fi)"
	@echo "Зависимости: $$(if [ -f venv/bin/activate ]; then . venv/bin/activate && pip list | wc -l | xargs echo 'установлено пакетов:'; else echo '❌ Не установлены'; fi)"
	@echo "Порт 8501: $$(lsof -i :8501 >/dev/null 2>&1 && echo '🔴 Занят' || echo '🟢 Свободен')"

check: ## Проверить готовность к запуску
	@echo "$(GREEN)🔍 Проверка готовности...$(NC)"
	@if [ ! -d venv ]; then echo "$(RED)❌ Виртуальное окружение не создано. Запустите: make install$(NC)"; exit 1; fi
	@if [ ! -f venv/bin/activate ]; then echo "$(RED)❌ Виртуальное окружение повреждено. Запустите: make clean && make install$(NC)"; exit 1; fi
	@if ! . venv/bin/activate && python -c "import streamlit" 2>/dev/null; then echo "$(RED)❌ Streamlit не установлен. Запустите: make install$(NC)"; exit 1; fi
	@echo "$(GREEN)✅ Все проверки пройдены!$(NC)"

.PHONY: all
all: install run ## Полная установка и запуск
