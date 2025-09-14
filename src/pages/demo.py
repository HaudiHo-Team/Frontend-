import streamlit as st
import time
import asyncio
import os
from src.components import header
from src.components import sidebar
from src.components import file_upload
from src.components import document_info
from src.components import file_viewer
from src.components import field_annotation
from src.api.api import Api

def render_demo_content():

    st.markdown("""
    <style>
    .main-container {
        display: flex;
        gap: 32px;
        align-items: flex-start;
    }

    .demo-main-content {
        padding: 20px;
        background: #0A0A0A;
        min-height: 100vh;
        flex: 1;
    }

    .demo-header {
        margin-bottom: 30px;
    }

    .demo-title {
        font-size: 28px;
        font-weight: 600;
        color: #FFFFFF;
        margin: 0 0 8px 0;
    }

    .demo-subtitle {
        font-size: 16px;
        color: #D8D8D8;
        margin: 0;
    }

    .demo-content-area {
        display: flex;
        gap: 20px;
        min-height: 600px;
    }

    .upload-section {
        flex: 1;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .files-section {
        flex: 1;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .section-title {
        font-size: 20px;
        font-weight: 500;
        color: #FFFFFF;
        margin: 0 0 20px 0;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 16px;
        margin-bottom: 24px;
    }

    .stat-card {
        background: rgba(149, 136, 212, 0.1);
        border: 1px solid rgba(149, 136, 212, 0.3);
        border-radius: 8px;
        padding: 16px;
        text-align: center;
    }

    .stat-number {
        font-size: 24px;
        font-weight: 600;
        color: #9588D4;
        margin: 0;
    }

    .stat-label {
        font-size: 14px;
        color: #D8D8D8;
        margin: 4px 0 0 0;
    }

    /* Адаптивность для мобильных устройств */
    @media (max-width: 768px) {
        .main-container {
            flex-direction: column;
            gap: 20px;
        }
        
        .demo-main-content {
            padding: 15px;
        }
        
        .demo-title {
            font-size: 24px;
        }
        
        .demo-content-area {
            flex-direction: column;
            gap: 15px;
        }
        
        .upload-section, .files-section {
            padding: 20px;
        }
        
        .stats-grid {
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 12px;
        }
        
        .stat-card {
            padding: 12px;
        }
        
        .stat-number {
            font-size: 20px;
        }
    }

    @media (max-width: 480px) {
        .demo-main-content {
            padding: 10px;
        }
        
        .demo-title {
            font-size: 20px;
        }
        
        .upload-section, .files-section {
            padding: 15px;
        }
        
        .stats-grid {
            grid-template-columns: 1fr;
        }
    }

    .process-button {
        background: linear-gradient(90deg, #9588D4 0%, #4D476E 100%) !important;
        border: none !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin-top: 16px !important;
    }

    .process-button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(149, 136, 212, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    [data-testid="stFileUploader"]{
      width:100% !important;
      max-width:100% !important;
    }

    [data-testid="stFileUploaderDropzone"]{
      border:2px dashed #9588D4 !important;
      background: rgba(149,136,212,0.05) !important;
      border-radius: 12px !important;

      padding: 40px !important;
      transition: transform .2s ease, box-shadow .2s ease, background .2s ease, border-color .2s ease !important;
      outline: none !important;
    }

    [data-testid="stFileUploaderDropzone"]:hover,
    [data-testid="stFileUploaderDropzone"]:focus,
    [data-testid="stFileUploaderDropzone"]:focus-within{
      border-color:#7A6BC7 !important;
      background: rgba(149,136,212,0.10) !important;
      box-shadow: 0 8px 30px rgba(149,136,212,0.25) !important;
      transform: translateY(-2px);
    }

    /* Внутренние инструкции */
    [data-testid="stFileUploaderDropzoneInstructions"]{
      display:flex !important;
      align-items:center !important;
      gap:16px !important;
      color:#FFFFFF !important;
    }

    /* Иконка (облако) — крупнее и полупрозрачная */
    [data-testid="stFileUploaderDropzoneInstructions"] svg{
      width:32px !important;
      height:32px !important;
      opacity:0.7 !important;
    }

    /* Тексты внутри инструкций: делаем первый span крупнее, остальные поменьше */
    [data-testid="stFileUploaderDropzoneInstructions"] span{
      display:block;
      line-height:1.3;
    }
    [data-testid="stFileUploaderDropzoneInstructions"] span:first-of-type{
      font-size:18px !important;
      font-weight:600 !important;
      color:#FFFFFF !important;
    }
    [data-testid="stFileUploaderDropzoneInstructions"] span:not(:first-of-type){
      font-size:14px !important;
      color:#D8D8D8 !important;
    }

    [data-testid="stFileUploader"] [data-testid="stBaseButton-secondary"]{
      background: linear-gradient(90deg, #9588D4 0%, #4D476E 100%) !important;
      border:none !important;
      color:#FFF !important;
      font-weight:600 !important;
      border-radius:8px !important;
      padding: 10px 16px !important;
      box-shadow:none !important;
      transition: transform .2s ease, box-shadow .2s ease !important;
    }
    [data-testid="stFileUploader"] [data-testid="stBaseButton-secondary"]:hover{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(149,136,212,0.3) !important;
    }

    /* Скрытый input — убираем артефакты */
    [data-testid="stFileUploaderDropzoneInput"]{
      outline:none !important;
      box-shadow:none !important;
      border:none !important;
    }
    
    /* Стили для кнопки обработки документов */
    .stButton > button {
        background: linear-gradient(135deg, #9588D4 0%, #4D476E 100%) !important;
        border: none !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        padding: 16px 32px !important;
        font-size: 18px !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin-top: 20px !important;
        box-shadow: 0 4px 16px rgba(149, 136, 212, 0.3) !important;
        text-transform: none !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 24px rgba(149, 136, 212, 0.4) !important;
        background: linear-gradient(135deg, #7A6BC7 0%, #3D3559 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    uploaded_files = file_upload.render_file_upload_area()
    if uploaded_files and hasattr(st.session_state, 'uploaded_file_id'):
        try:
            api = Api()
            file_info = api.get_file(st.session_state.uploaded_file_id)
            
            if os.getenv("DEBUG", "false").lower() == "true":
                st.write("Debug - API response type:", type(file_info))
                st.write("Debug - API response content:", file_info)
            
            if isinstance(file_info, str):
                st.warning("API вернул строку вместо JSON. Попробуйте еще раз.")
                st.write("Debug - API response:", file_info)
                return
            
            file_data = None
            if uploaded_files:
                file_data = uploaded_files[0]['file'].read()
                uploaded_files[0]['file'].seek(0)
            
            st.markdown("### 📄 Загруженный документ")
            file_viewer.render_simple_file_display(
                filename=file_info.get('filename', 'Неизвестный файл'),
                coordinates=None,
                file_data=file_data
            )
            
            if file_data and file_info.get('filename', '').lower().endswith('.pdf'):
                field_annotation.render_field_annotation(
                    file_data=file_data,
                    filename=file_info.get('filename', 'Неизвестный файл'),
                    coordinates=None
                )
            
        except Exception as e:
            st.error(f"Ошибка при загрузке информации о файле: {str(e)}")
    
    if uploaded_files and st.button("🚀 Обработать документы", type="primary", use_container_width=True):
        api = Api()
        
        st.session_state.document_processing = True
        st.session_state.document_data = {"loading": True}
        st.session_state.processing_start_time = time.time()
        
        if uploaded_files:
            file_info = uploaded_files[0]
            file_data = file_info['file'].read()
            
            st.session_state.uploaded_files = uploaded_files
            
            try:
                response = api.upload_file(
                    file_data=file_data,
                    filename=file_info['name'],
                    content_type=file_info['type']
                )
                
                st.session_state.uploaded_file_id = response.get('id')
                st.session_state.upload_status = response.get('status')
                
            except Exception as e:
                st.error(f"Ошибка при загрузке файла: {str(e)}")
                st.session_state.document_processing = False
                st.session_state.document_data = None
        
        st.rerun()
    
    if (hasattr(st.session_state, 'processing_start_time') and 
        hasattr(st.session_state, 'document_processing') and 
        st.session_state.document_processing):
        
        elapsed_time = time.time() - st.session_state.processing_start_time
        
        if hasattr(st.session_state, 'uploaded_file_id'):
            try:
                api = Api()
                file_info = api.get_file(st.session_state.uploaded_file_id)
                
                if isinstance(file_info, str):
                    st.warning("API вернул строку вместо JSON. Попробуйте еще раз.")
                    st.write("Debug - API response:", file_info)
                    return
                
                file_data = None
                if hasattr(st.session_state, 'uploaded_files') and st.session_state.uploaded_files:
                    file_data = st.session_state.uploaded_files[0]['file'].read()
                    st.session_state.uploaded_files[0]['file'].seek(0)
                
                st.markdown("### 📄 Обрабатываемый документ")
                file_viewer.render_simple_file_display(
                    filename=file_info.get('filename', 'Неизвестный файл'),
                    coordinates=None,
                    file_data=file_data
                )
                
                if file_info.get('processed_result') and file_info['processed_result'].get('data'):
                    import json
                    try:
                        result_data = json.loads(file_info['processed_result']['data'])
                        
                        document_data = {
                            "contract_number": result_data.get("contract_number", "—"),
                            "contract_start_date": result_data.get("contract_start_date", "—"),
                            "contract_end_date": result_data.get("contract_end_date", "—"),
                            "counterparty": result_data.get("counterparty", "—"),
                            "country": result_data.get("country", "—"),
                            "contract_amount": result_data.get("contract_amount", "—"),
                            "contract_currency": result_data.get("contract_currency", "—"),
                            "payment_currency": result_data.get("payment_currency", "—")
                        }
                        
                        st.session_state.document_data = document_data
                        st.session_state.document_processing = False
                        st.success("✅ Документ успешно обработан!")
                        
                    except json.JSONDecodeError:
                        st.session_state.document_data = {
                            "contract_number": "—",
                            "contract_start_date": "—",
                            "contract_end_date": "—",
                            "counterparty": "—",
                            "country": "—",
                            "contract_amount": "—",
                            "contract_currency": "—",
                            "payment_currency": "—"
                        }
                        st.session_state.document_processing = False
                        st.warning("⚠️ Данные получены, но в неожиданном формате")
                else:
                    if elapsed_time < 30:
                        st.info("⏳ Ожидание завершения обработки...")
                    else:
                        st.session_state.document_processing = False
                        st.error("❌ Время ожидания истекло. Попробуйте еще раз.")
                        
            except Exception as e:
                st.session_state.document_processing = False
                st.error(f"Ошибка при получении результата: {str(e)}")
        else:
            st.session_state.document_processing = False
            st.error("❌ Ошибка: не найден ID загруженного файла")
        
        time.sleep(1)
        st.rerun()

    if hasattr(st.session_state, 'document_data') and st.session_state.document_data:
        document_info.render_document_info(st.session_state.document_data)
        
        if hasattr(st.session_state, 'uploaded_file_id'):
            try:
                api = Api()
                file_info = api.get_file(st.session_state.uploaded_file_id)
                
                if isinstance(file_info, str):
                    st.warning("API вернул строку вместо JSON. Попробуйте еще раз.")
                    st.write("Debug - API response:", file_info)
                    return
                
                file_data = None
                if hasattr(st.session_state, 'uploaded_files') and st.session_state.uploaded_files:
                    file_data = st.session_state.uploaded_files[0]['file'].read()
                    st.session_state.uploaded_files[0]['file'].seek(0)
                
                coordinates = None
                if file_info.get('processed_result') and file_info['processed_result'].get('data'):
                    import json
                    try:
                        result_data = json.loads(file_info['processed_result']['data'])
                        coordinates = result_data.get('coordinates', [])
                    except:
                        coordinates = []
                
                if coordinates:
                    st.markdown("### 📄 Просмотр документа с координатами")
                    file_viewer.render_file_viewer(
                        file_data=file_info,
                        coordinates=coordinates
                    )
                else:
                    file_viewer.render_simple_file_display(
                        filename=file_info.get('filename', 'Неизвестный файл'),
                        coordinates=coordinates,
                        file_data=file_data
                    )
                    
            except Exception as e:
                st.error(f"Ошибка при загрузке файла: {str(e)}")


def render_demo_page():
    header.render_page_header()

    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        sidebar.render_sidebar()

    with col2:
        render_demo_content()

    st.markdown('</div>', unsafe_allow_html=True)
