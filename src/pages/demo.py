import streamlit as st

def render_demo_header():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');

    html {
        scroll-behavior: smooth;
    }

    .stDeployButton {
        display: none !important;
    }

    .stDecoration {
        display: none !important;
    }

    .stStatusWidget {
        display: none !important;
    }

    .stProgress {
        display: none !important;
    }

    .stException {
        display: none !important;
    }

    .main .block-container {
        padding-top: 80px !important;
    }

    .demo-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        padding: 1rem 2rem;
    }

    .demo-header-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
        font-family: 'Montserrat', sans-serif !important;
    }

    .demo-logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
    }

    .demo-nav {
        display: flex;
        gap: 2rem;
        align-items: center;
    }

    .demo-nav-link {
        color: white !important;
        text-decoration: none;
        font-weight: 500;
        transition: opacity 0.3s;
    }

    .demo-nav-link:hover {
        opacity: 0.8;
    }

    .demo-back-btn {
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.3s;
    }

    .demo-back-btn:hover {
        background: rgba(255, 255, 255, 0.3);
        color: white;
        text-decoration: none;
    }

    .demo-sidebar {
        position: fixed;
        left: 0;
        top: 80px;
        width: 250px;
        height: calc(100vh - 80px);
        background: #f8f9fa;
        border-right: 1px solid #e9ecef;
        padding: 2rem 1rem;
        overflow-y: auto;
        z-index: 999;
    }

    .demo-main-content {
        margin-left: 250px;
        padding: 2rem;
        min-height: calc(100vh - 80px);
    }

    .demo-section {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .demo-section h2 {
        color: #333;
        margin-bottom: 1rem;
        font-family: 'Montserrat', sans-serif;
    }

    .demo-section p {
        color: #666;
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .demo-feature {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
        margin-bottom: 1rem;
    }

    .demo-feature-icon {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
    }

    .demo-feature-text {
        flex: 1;
    }

    .demo-feature-text h4 {
        margin: 0 0 0.5rem 0;
        color: #333;
    }

    .demo-feature-text p {
        margin: 0;
        color: #666;
        font-size: 0.9rem;
    }

    @media (max-width: 768px) {
        .demo-sidebar {
            display: none;
        }
        
        .demo-main-content {
            margin-left: 0;
        }
        
        .demo-nav {
            display: none;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="demo-header">
        <div class="demo-header-content">
            <div class="demo-logo">
                <span>🚀</span>
                <span>ContractAI Demo</span>
            </div>
            <div class="demo-nav">
                <a href="#features" class="demo-nav-link">Возможности</a>
                <a href="#how-it-works" class="demo-nav-link">Как работает</a>
                <a href="#pricing" class="demo-nav-link">Тарифы</a>
                <a href="?" class="demo-back-btn">← Назад</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_demo_sidebar():
    st.markdown("""
    <div class="demo-sidebar">
        <h3 style="color: #333; margin-bottom: 1.5rem;">Навигация</h3>
        <nav style="display: flex; flex-direction: column; gap: 0.5rem;">
            <a href="#overview" style="color: #666; text-decoration: none; padding: 0.5rem; border-radius: 6px; transition: background 0.3s;">📋 Обзор</a>
            <a href="#features" style="color: #666; text-decoration: none; padding: 0.5rem; border-radius: 6px; transition: background 0.3s;">⚡ Возможности</a>
            <a href="#how-it-works" style="color: #666; text-decoration: none; padding: 0.5rem; border-radius: 6px; transition: background 0.3s;">🔧 Как работает</a>
            <a href="#pricing" style="color: #666; text-decoration: none; padding: 0.5rem; border-radius: 6px; transition: background 0.3s;">💰 Тарифы</a>
            <a href="#contact" style="color: #666; text-decoration: none; padding: 0.5rem; border-radius: 6px; transition: background 0.3s;">📞 Контакты</a>
        </nav>
        
        <div style="margin-top: 2rem; padding: 1rem; background: #e3f2fd; border-radius: 8px;">
            <h4 style="color: #1976d2; margin: 0 0 0.5rem 0;">Попробовать сейчас</h4>
            <p style="color: #666; font-size: 0.9rem; margin: 0 0 1rem 0;">Загрузите свой контракт и посмотрите, как работает AI</p>
            <button style="width: 100%; background: #1976d2; color: white; border: none; padding: 0.75rem; border-radius: 6px; font-weight: 500; cursor: pointer;">Загрузить файл</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_demo_content():
    st.markdown("""
    <div class="demo-main-content">
        <div id="overview" class="demo-section">
            <h2>Добро пожаловать в демо ContractAI</h2>
            <p>Это интерактивная демонстрация возможностей нашего AI-решения для анализа контрактов. Здесь вы можете увидеть, как работает система в реальном времени.</p>
            
            <div class="demo-feature">
                <div class="demo-feature-icon">📄</div>
                <div class="demo-feature-text">
                    <h4>Загрузка контракта</h4>
                    <p>Загрузите любой PDF или Word документ с контрактом</p>
                </div>
            </div>
            
            <div class="demo-feature">
                <div class="demo-feature-icon">🤖</div>
                <div class="demo-feature-text">
                    <h4>AI анализ</h4>
                    <p>Наш AI проанализирует документ и выделит ключевые моменты</p>
                </div>
            </div>
            
            <div class="demo-feature">
                <div class="demo-feature-icon">📊</div>
                <div class="demo-feature-text">
                    <h4>Результаты</h4>
                    <p>Получите детальный отчет с рекомендациями и рисками</p>
                </div>
            </div>
        </div>

        <div id="features" class="demo-section">
            <h2>Основные возможности</h2>
            <p>ContractAI предоставляет мощные инструменты для анализа контрактов:</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin-top: 1.5rem;">
                <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px;">
                    <h4 style="color: #333; margin-bottom: 1rem;">🔍 Анализ рисков</h4>
                    <p style="color: #666; margin: 0;">Автоматическое выявление потенциальных рисков и проблемных мест в контрактах</p>
                </div>
                
                <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px;">
                    <h4 style="color: #333; margin-bottom: 1rem;">📝 Извлечение данных</h4>
                    <p style="color: #666; margin: 0;">Автоматическое извлечение ключевых данных: даты, суммы, стороны договора</p>
                </div>
                
                <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px;">
                    <h4 style="color: #333; margin-bottom: 1rem;">⚖️ Соответствие законам</h4>
                    <p style="color: #666; margin: 0;">Проверка соответствия контракта действующему законодательству</p>
                </div>
                
                <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px;">
                    <h4 style="color: #333; margin-bottom: 1rem;">📈 Рекомендации</h4>
                    <p style="color: #666; margin: 0;">Персональные рекомендации по улучшению контракта</p>
                </div>
            </div>
        </div>

        <div id="how-it-works" class="demo-section">
            <h2>Как это работает</h2>
            <p>Простой процесс анализа контрактов в несколько шагов:</p>
            
            <div style="display: flex; flex-direction: column; gap: 1.5rem; margin-top: 1.5rem;">
                <div style="display: flex; align-items: center; gap: 1rem; padding: 1rem; background: #e8f5e8; border-radius: 8px;">
                    <div style="width: 40px; height: 40px; background: #4caf50; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">1</div>
                    <div>
                        <h4 style="margin: 0 0 0.5rem 0; color: #333;">Загрузите контракт</h4>
                        <p style="margin: 0; color: #666;">Выберите файл PDF или Word с вашим контрактом</p>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center; gap: 1rem; padding: 1rem; background: #e3f2fd; border-radius: 8px;">
                    <div style="width: 40px; height: 40px; background: #2196f3; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">2</div>
                    <div>
                        <h4 style="margin: 0 0 0.5rem 0; color: #333;">AI анализирует</h4>
                        <p style="margin: 0; color: #666;">Наш искусственный интеллект изучает документ и выделяет ключевые моменты</p>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center; gap: 1rem; padding: 1rem; background: #fff3e0; border-radius: 8px;">
                    <div style="width: 40px; height: 40px; background: #ff9800; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">3</div>
                    <div>
                        <h4 style="margin: 0 0 0.5rem 0; color: #333;">Получите результат</h4>
                        <p style="margin: 0; color: #666;">Скачайте детальный отчет с анализом и рекомендациями</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="pricing" class="demo-section">
            <h2>Тарифные планы</h2>
            <p>Выберите подходящий план для ваших потребностей:</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
                <div style="padding: 2rem; border: 2px solid #e9ecef; border-radius: 12px; text-align: center;">
                    <h3 style="color: #333; margin-bottom: 1rem;">Базовый</h3>
                    <div style="font-size: 2rem; font-weight: bold; color: #333; margin-bottom: 1rem;">₽0</div>
                    <p style="color: #666; margin-bottom: 1.5rem;">Для ознакомления</p>
                    <ul style="text-align: left; color: #666; margin-bottom: 2rem;">
                        <li>5 контрактов в месяц</li>
                        <li>Базовый анализ</li>
                        <li>Email поддержка</li>
                    </ul>
                    <button style="width: 100%; background: #6c757d; color: white; border: none; padding: 0.75rem; border-radius: 6px; font-weight: 500;">Выбрать</button>
                </div>
                
                <div style="padding: 2rem; border: 2px solid #007bff; border-radius: 12px; text-align: center; position: relative;">
                    <div style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%); background: #007bff; color: white; padding: 0.25rem 1rem; border-radius: 20px; font-size: 0.8rem;">Популярный</div>
                    <h3 style="color: #333; margin-bottom: 1rem;">Профессиональный</h3>
                    <div style="font-size: 2rem; font-weight: bold; color: #333; margin-bottom: 1rem;">₽2,990</div>
                    <p style="color: #666; margin-bottom: 1.5rem;">в месяц</p>
                    <ul style="text-align: left; color: #666; margin-bottom: 2rem;">
                        <li>50 контрактов в месяц</li>
                        <li>Расширенный анализ</li>
                        <li>Приоритетная поддержка</li>
                        <li>API доступ</li>
                    </ul>
                    <button style="width: 100%; background: #007bff; color: white; border: none; padding: 0.75rem; border-radius: 6px; font-weight: 500;">Выбрать</button>
                </div>
                
                <div style="padding: 2rem; border: 2px solid #e9ecef; border-radius: 12px; text-align: center;">
                    <h3 style="color: #333; margin-bottom: 1rem;">Корпоративный</h3>
                    <div style="font-size: 2rem; font-weight: bold; color: #333; margin-bottom: 1rem;">₽9,990</div>
                    <p style="color: #666; margin-bottom: 1.5rem;">в месяц</p>
                    <ul style="text-align: left; color: #666; margin-bottom: 2rem;">
                        <li>Безлимитные контракты</li>
                        <li>Полный анализ</li>
                        <li>Персональный менеджер</li>
                        <li>Интеграции</li>
                    </ul>
                    <button style="width: 100%; background: #6c757d; color: white; border: none; padding: 0.75rem; border-radius: 6px; font-weight: 500;">Связаться</button>
                </div>
            </div>
        </div>

        <div id="contact" class="demo-section">
            <h2>Свяжитесь с нами</h2>
            <p>Готовы начать? Свяжитесь с нашей командой для получения персональной консультации.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
                <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
                    <h4 style="color: #333; margin-bottom: 1rem;">📧 Email</h4>
                    <p style="color: #666; margin: 0;">info@contractai.ru</p>
                </div>
                
                <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
                    <h4 style="color: #333; margin-bottom: 1rem;">📞 Телефон</h4>
                    <p style="color: #666; margin: 0;">+7 (495) 123-45-67</p>
                </div>
                
                <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; text-align: center;">
                    <h4 style="color: #333; margin-bottom: 1rem;">💬 Telegram</h4>
                    <p style="color: #666; margin: 0;">@contractai_support</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_demo_page():
    render_demo_header()
    render_demo_sidebar()
    render_demo_content()
