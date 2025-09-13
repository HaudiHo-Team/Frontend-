#!/usr/bin/env python3
"""
Скрипт запуска Streamlit приложения
"""

import subprocess
import sys
import os

def main():
    """Главная функция запуска"""
    
    # Проверка наличия Streamlit
    try:
        import streamlit
    except ImportError:
        print("❌ Streamlit не установлен. Установите зависимости:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    # Проверка наличия основного файла
    if not os.path.exists("app.py"):
        print("❌ Файл app.py не найден")
        sys.exit(1)
    
    # Параметры запуска
    cmd = [
        "streamlit", "run", "app.py",
        "--server.port", "8501",
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false"
    ]
    
    print("🚀 Запуск Frontend App...")
    print("📱 Откройте браузер по адресу: http://localhost:8501")
    print("⏹️  Для остановки нажмите Ctrl+C")
    print("-" * 50)
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n👋 Приложение остановлено")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка запуска: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
