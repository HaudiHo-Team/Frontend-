"""
Пример использования API
"""

import streamlit as st
from src.api.api import get_api, upload_file_to_api, quick_extract_text, quick_search, login_user, logout_user

def render_api_example():
    """Демонстрация работы с API"""
    
    st.title("🔌 Пример работы с API")
    
    # Получаем API клиент
    api = get_api()
    
    # Проверяем аутентификацию
    auth_status = api.get_auth_status()
    
    if not auth_status["authenticated"]:
        st.warning("⚠️ Необходима авторизация для работы с API")
        
        # Форма авторизации
        with st.form("login_form"):
            st.subheader("Вход в систему")
            email = st.text_input("Email")
            password = st.text_input("Пароль", type="password")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("Войти"):
                    if login_user(email, password):
                        st.success("Успешная авторизация!")
                        st.rerun()
                    else:
                        st.error("Ошибка авторизации")
            
            with col2:
                if st.form_submit_button("Регистрация"):
                    # Здесь можно добавить форму регистрации
                    st.info("Функция регистрации будет добавлена")
    
    else:
        st.success(f"✅ Авторизован как: {auth_status.get('user', {}).get('name', 'Пользователь')}")
        
        # Кнопка выхода
        if st.button("Выйти"):
            logout_user()
            st.rerun()
        
        st.divider()
        
        # Вкладки для разных функций
        tab1, tab2, tab3, tab4 = st.tabs(["📁 Файлы", "📄 Документы", "🔍 Поиск", "📊 Аналитика"])
        
        with tab1:
            render_files_tab(api)
        
        with tab2:
            render_documents_tab(api)
        
        with tab3:
            render_search_tab(api)
        
        with tab4:
            render_analytics_tab(api)

def render_files_tab(api):
    """Вкладка работы с файлами"""
    st.subheader("Управление файлами")
    
    # Загрузка файлов
    uploaded_files = st.file_uploader(
        "Выберите файлы для загрузки",
        accept_multiple_files=True,
        type=['pdf', 'doc', 'docx', 'txt']
    )
    
    if uploaded_files:
        if st.button("Загрузить файлы"):
            with st.spinner("Загрузка файлов..."):
                for uploaded_file in uploaded_files:
                    file_id = upload_file_to_api(uploaded_file)
                    if file_id:
                        st.write(f"✅ {uploaded_file.name} → ID: {file_id}")
    
    st.divider()
    
    # Список файлов
    st.subheader("Список файлов")
    if st.button("Обновить список"):
        try:
            files = api.get_files()
            if files and "files" in files:
                for file_info in files["files"]:
                    col1, col2, col3 = st.columns([3, 1, 1])
                    
                    with col1:
                        st.write(f"📄 {file_info.get('name', 'Неизвестный файл')}")
                    
                    with col2:
                        if st.button("Скачать", key=f"download_{file_info.get('id')}"):
                            file_data = api.get_file(file_info.get('id'))
                            if file_data:
                                st.download_button(
                                    "Скачать файл",
                                    file_data,
                                    file_name=file_info.get('name'),
                                    key=f"dl_{file_info.get('id')}"
                                )
                    
                    with col3:
                        if st.button("Удалить", key=f"delete_{file_info.get('id')}"):
                            if api.delete_file(file_info.get('id')):
                                st.success("Файл удален!")
                                st.rerun()
            else:
                st.info("Файлы не найдены")
        except Exception as e:
            st.error(f"Ошибка получения файлов: {str(e)}")

def render_documents_tab(api):
    """Вкладка работы с документами"""
    st.subheader("Обработка документов")
    
    # Получаем список файлов для обработки
    try:
        files = api.get_files()
        if files and "files" in files:
            file_options = {f"{f['name']} (ID: {f['id']})": f['id'] for f in files["files"]}
            
            if file_options:
                selected_file = st.selectbox("Выберите файл для обработки", list(file_options.keys()))
                
                if selected_file:
                    file_id = file_options[selected_file]
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        if st.button("Извлечь текст"):
                            with st.spinner("Извлечение текста..."):
                                text = quick_extract_text(file_id)
                                if text:
                                    st.text_area("Извлеченный текст", text, height=200)
                                else:
                                    st.warning("Не удалось извлечь текст")
                    
                    with col2:
                        if st.button("Анализировать"):
                            with st.spinner("Анализ документа..."):
                                analysis = api.analyze_document(file_id)
                                st.json(analysis)
                    
                    with col3:
                        target_format = st.selectbox("Формат", ["pdf", "docx", "txt"])
                        if st.button("Конвертировать"):
                            with st.spinner("Конвертация..."):
                                result = api.convert_document(file_id, target_format)
                                st.json(result)
            else:
                st.info("Нет файлов для обработки")
        else:
            st.info("Файлы не найдены")
    except Exception as e:
        st.error(f"Ошибка: {str(e)}")

def render_search_tab(api):
    """Вкладка поиска"""
    st.subheader("Поиск в документах")
    
    query = st.text_input("Введите поисковый запрос:")
    
    if st.button("Поиск") and query:
        with st.spinner("Поиск..."):
            try:
                results = quick_search(query)
                
                if results:
                    st.write(f"Найдено {len(results)} результатов:")
                    
                    for i, result in enumerate(results):
                        with st.expander(f"Результат {i+1}: {result.get('filename', 'Неизвестный файл')}"):
                            st.write(f"**Текст:** {result.get('text', '')}")
                            st.write(f"**Страница:** {result.get('page', 'N/A')}")
                            st.write(f"**Файл ID:** {result.get('file_id', 'N/A')}")
                else:
                    st.info("Результаты не найдены")
            except Exception as e:
                st.error(f"Ошибка поиска: {str(e)}")

def render_analytics_tab(api):
    """Вкладка аналитики"""
    st.subheader("Аналитика")
    
    try:
        # Статистика загрузок
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Всего файлов", "0", "0")
        
        with col2:
            st.metric("Обработано", "0", "0")
        
        with col3:
            st.metric("Ошибок", "0", "0")
        
        # Детальная статистика
        if st.button("Обновить статистику"):
            with st.spinner("Загрузка статистики..."):
                try:
                    upload_stats = api.get_upload_stats()
                    processing_stats = api.get_processing_stats()
                    activity = api.get_user_activity()
                    
                    st.success("Статистика обновлена!")
                    
                    # Отображаем статистику
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Загрузки")
                        st.json(upload_stats)
                    
                    with col2:
                        st.subheader("Обработка")
                        st.json(processing_stats)
                    
                    st.subheader("Активность")
                    st.json(activity)
                    
                except Exception as e:
                    st.error(f"Ошибка загрузки статистики: {str(e)}")
    
    except Exception as e:
        st.error(f"Ошибка: {str(e)}")

def render_api_example_page():
    """Основная страница с примером API"""
    from src.components import header, sidebar
    
    header.render_page_header()
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        sidebar.render_sidebar()
    
    with col2:
        render_api_example()
    
    st.markdown('</div>', unsafe_allow_html=True)
