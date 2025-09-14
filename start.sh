#!/bin/bash

# Frontend App - Скрипт быстрого запуска
# Использование: ./start.sh

set -e  # Остановка при ошибке

# Цвета для вывода
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Frontend App - Быстрый запуск${NC}"
echo ""

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 не найден. Установите Python 3.8+${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Python найден: $(python3 --version)${NC}"

# Проверка виртуального окружения
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}📦 Создание виртуального окружения...${NC}"
    python3 -m venv venv
fi

# Активация виртуального окружения
echo -e "${GREEN}🔧 Активация виртуального окружения...${NC}"
source venv/bin/activate

# Проверка зависимостей
if [ ! -f "venv/bin/streamlit" ]; then
    echo -e "${YELLOW}📦 Установка зависимостей...${NC}"
    pip install --upgrade pip
    pip install -r requirements.txt
fi

echo -e "${GREEN}✅ Все готово!${NC}"
echo ""
echo -e "${GREEN}🚀 Запуск приложения...${NC}"
echo -e "${YELLOW}📱 Откройте браузер по адресу: http://localhost:8501${NC}"
echo -e "${YELLOW}⏹️  Для остановки нажмите Ctrl+C${NC}"
echo ""

# Запуск приложения
python run.py
