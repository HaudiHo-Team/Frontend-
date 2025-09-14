import streamlit as st
import streamlit.components.v1 as components
from src.utils import load_icon

def render_file_upload_area():

    upload_icon = load_icon("src/assets/icons/plus.svg", 96, 96)
    plus_icon = load_icon("src/assets/icons/plus.svg", 24, 24)

    st.markdown("""
    <style>
    .upload-area {
        border: 2px dashed #9588D4;
        border-radius: 12px;
        padding: 40px;
        text-align: center;
        background: rgba(149, 136, 212, 0.05);
        transition: all 0.3s ease;
        cursor: pointer;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 16px;
        position: relative;
        user-select: none;
    }

    .upload-area:hover {
        border-color: #7A6BC7;
        background: rgba(149, 136, 212, 0.1);
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(149, 136, 212, 0.2);
    }

    .upload-area.dragover {
        border-color: #7A6BC7;
        background: rgba(149, 136, 212, 0.15);
        transform: scale(1.02);
        box-shadow: 0 8px 30px rgba(149, 136, 212, 0.3);
    }

    .upload-area:active {
        transform: scale(0.98);
    }

    .upload-icon {
        opacity: 0.7;
    }

    .upload-text {
        font-size: 18px;
        color: #FFFFFF;
        font-weight: 500;
        margin: 0;
    }

    .upload-subtext {
        font-size: 14px;
        color: #D8D8D8;
        margin: 0;
    }

    .upload-area.dragover .upload-text {
        color: #7A6BC7;
        font-weight: 600;
    }

    .upload-area.dragover .upload-subtext {
        color: #9588D4;
    }

    .upload-area.dragover .upload-icon {
        opacity: 1;
        transform: scale(1.1);
    }

    .upload-button {
        background: linear-gradient(90deg, #9588D4 0%, #4D476E 100%);
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        color: white;
        font-size: 16px;
        font-weight: 500;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: all 0.3s ease;
    }

    .upload-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(149, 136, 212, 0.3);
    }

    </style>
    """, unsafe_allow_html=True)

    # Инициализация session state для файлов
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = []

    uploaded_files = st.file_uploader(
        "Перетащите файлы сюда или нажмите для выбора",
        type=['pdf', 'doc', 'docx'],
        accept_multiple_files=True,
        key="file-upload",
        help="Поддерживаемые форматы: PDF, DOC, DOCX"
    )

    if uploaded_files:
        for uploaded_file in uploaded_files:
            if uploaded_file not in st.session_state.uploaded_files:
                st.session_state.uploaded_files.append({
                    'name': uploaded_file.name,
                    'size': uploaded_file.size,
                    'type': uploaded_file.type,
                    'file': uploaded_file
                })

    return st.session_state.uploaded_files
