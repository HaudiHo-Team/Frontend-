"""
Главный файл Streamlit приложения
Архитектура: Модульная структура с разделением на компоненты и страницы
"""

import streamlit as st
import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.pages import home
from src.config.app_config import AppConfig

st.set_page_config(
    page_title="Frontend App",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
</style>
""", unsafe_allow_html=True)


def main():
    config = AppConfig()
    home.render()

if __name__ == "__main__":
    main()
