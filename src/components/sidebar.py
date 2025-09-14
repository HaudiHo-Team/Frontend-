import streamlit as st
import streamlit.components.v1 as components
from src.utils import load_icon

def render_sidebar():
    upload_docs_icon = load_icon("src/assets/icons/upload.svg", 24, 24)
    magnificent_find_icon = load_icon("src/assets/icons/magnificent.svg", 24, 24)
    dir_add_icon = load_icon("src/assets/icons/dir-add.svg", 24, 24)
    dir_icon = load_icon("src/assets/icons/dir.svg", 24, 24)

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');
        .sidebar {
                width:fit-content;
               border: 1px solid transparent;
                    background:
                      linear-gradient(#0A0A0A, #0A0A0A) padding-box,
                      linear-gradient(90deg, #9588D4 47%, #4D476E 100%) border-box;
                    -webkit-background-clip: padding-box, border-box;
                    background-clip: padding-box, border-box;
                    -webkit-text-fill-color: initial;
                    border-radius: 20px;
        }
        .sidebar-content {
            padding: 25px 45px;
            display: flex;
            flex-direction: column ;
            align-items: start ;
            gap: 32px;
        }
        .sidebar-actions {
            display: flex;
            flex-direction: column;
            gap:21px;
            align-items: start
        }
        .sidebar-item {
            display: flex;
            gap: 8px;
            align-items: center;
            justify-content: start;
        }

        .sidebar-name {
            font-size: 17px !important;
            color:#ffffff;
        }

        .checked-files-section {
            display:flex;
            align-items: start;
            gap:12px;
            flex-direction: column;
        }

        .checked-files-title {
            font-size: 19px;
            font-weight: 500;
            color: #FFFFFF;
        }

        .checked-files-list {
            display:flex;
            flex-direction: column;
            gap: 9px;
            align-items: start;
        }

        .file-item {
            font-size: 17px;
            color: #D8D8D8;
        }


    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="sidebar">
        <div class="sidebar-content">
            <div class="sidebar-actions">
                <div class="sidebar-item" id="upload-document">
                    { upload_docs_icon }
                    <span class="sidebar-name">Загрузить документ</span>
                </div>
                <div class="sidebar-item" id="find-document">
                    { magnificent_find_icon }
                    <span class="sidebar-name">Поиск документов</span>
                </div>
                <div class="sidebar-item" id="dir-add">
                    { dir_add_icon }
                    <span class="sidebar-name">Новая папка</span>
                </div>
                <div class="dir-list">
                    <div class="sidebar-item">
                            { dir_icon }
                             <span class="sidebar-name">БЦК</span>
                    </div>
                </div>
            </div>
            <div class="checked-files-section">
                <span class="checked-files-title">
                    Проверенные файлы:
                </span>
                <div class="checked-files-list">
                    <span class="file-item">
                      Contract_agreement_Astana2025.pdf
                    </span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
