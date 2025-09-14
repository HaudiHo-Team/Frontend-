import streamlit as st
import requests
import os
from src.api.api import Api

def check_api_health():
    try:
        api = Api()
        response = api.get("/files/", params={"limit": 1})
        return True, "API доступен"
    except Exception as e:
        return False, f"API недоступен: {str(e)}"

def get_health_status():
    api_healthy, api_message = check_api_health()
    
    return {
        "status": "healthy" if api_healthy else "unhealthy",
        "api": {
            "status": "up" if api_healthy else "down",
            "message": api_message
        },
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "development")
    }

def render_health_page():
    st.set_page_config(
        page_title="Health Check",
        page_icon="🏥",
        layout="centered"
    )
    
    st.title("🏥 Health Check")
    
    health_status = get_health_status()
    
    if health_status["status"] == "healthy":
        st.success("✅ Приложение работает нормально")
    else:
        st.error("❌ Обнаружены проблемы")
    
    st.json(health_status)
    
    # Кнопка для обновления статуса
    if st.button("🔄 Обновить статус"):
        st.rerun()

if __name__ == "__main__":
    render_health_page()
