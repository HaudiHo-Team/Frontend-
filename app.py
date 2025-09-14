"""
Главный файл Streamlit приложения
Архитектура: Модульная структура с разделением на компоненты и страницы
"""

import streamlit as st
import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.pages import home, demo
from src.config.app_config import AppConfig

st.set_page_config(
    page_title="ContractAI",
    page_icon="🚀",
    layout="wide"
)

def main():
    config = AppConfig()
    
    query_params = st.query_params
    
    if 'page' in query_params and query_params['page'] == 'demo':
        demo.render_demo_page()
    else:
        home.render()

if __name__ == "__main__":
    main()
