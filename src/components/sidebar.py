import streamlit as st
from src.api.api import Api

def render_sidebar():

    # Получаем список файлов с API
    try:
        api = Api()
        files_response = api.get_files_list()
        files_list = files_response.get('items', []) if isinstance(files_response, dict) else []
    except Exception as e:
        st.error(f"Ошибка загрузки файлов: {str(e)}")
        files_list = []

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');
        .sidebar {
                width:100%;
               border: 1px solid transparent;
                    background:
                      linear-gradient(#0A0A0A, #0A0A0A) padding-box,
                      linear-gradient(90deg, #9588D4 47%, #4D476E 100%) border-box;
                    -webkit-background-clip: padding-box, border-box;
                    background-clip: padding-box, border-box;
                    -webkit-text-fill-color: initial;
                    border-radius: 20px 20px 20px 0 ;
        }
        .sidebar-content {
            padding: 12px 16px;
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
            padding: 8px 12px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .sidebar-item:hover {
            background: rgba(149, 136, 212, 0.1);
            border-color: rgba(149, 136, 212, 0.3);
            transform: translateX(2px);
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
            padding: 8px 16px;
            background: rgba(149, 136, 212, 0.1);
            border: 1px solid rgba(149, 136, 212, 0.3);
            border-radius: 8px;
            margin-bottom: 8px;
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
        padding: 8px 12px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(149, 136, 212, 0.3);
        transition: all 0.3s ease;
        cursor: pointer;
        display: flex;
        align-items: center;
        min-height: 40px;
        width: 100%;
    }

    .file-item:hover {
        background: rgba(149, 136, 212, 0.1);
        border-color: rgba(149, 136, 212, 0.6);
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(149, 136, 212, 0.2);
    }

    .file-name {
        flex: 1;
    }

    .stButton {
        margin: 0 !important;
        padding: 0 !important;
    }

    .stButton > button {
        background: rgba(255, 0, 0, 0.1) !important;
        border: 2px solid rgba(255, 0, 0, 0.5) !important;
        color: #ff6b6b !important;
        border-radius: 6px !important;
        padding: 4px 8px !important;
        font-size: 14px !important;
        transition: all 0.3s ease !important;
        margin: 0 !important;
        min-height: 30px !important;
        width: 30px !important;
        position: relative !important;
        right: 0 !important;
        top: 0 !important;
        transform: none !important;
        flex-shrink: 0 !important;
    }

    .stButton > button:hover {
        background: rgba(255, 0, 0, 0.2) !important;
        border-color: rgba(255, 0, 0, 0.8) !important;
        transform: scale(1.1) !important;
        box-shadow: 0 2px 8px rgba(255, 0, 0, 0.3) !important;
    }

    .file-item {
        position: relative !important;
    }

    /* Стили для колонок с файлами */
    .stColumn {
        display: flex !important;
        align-items: center !important;
    }

    .stColumn:first-child {
        flex: 1 !important;
    }

    .stColumn:last-child {
        flex: 0 0 auto !important;
        margin-left: 8px !important;
    }


        .no-files {
            font-size: 14px;
            color: #6B7280;
            font-style: italic;
            text-align: center;
            padding: 20px;
        }


    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar">
        <div class="sidebar-content">
            <div class="checked-files-section">
                <span class="checked-files-title">Загруженные файлы:</span>
                <div class="checked-files-list">
    """, unsafe_allow_html=True)

    if files_list:
        for i, file_info in enumerate(files_list):
            filename = file_info.get('filename', 'Неизвестный файл')
            file_id = file_info.get('id', '')

            col1, col2 = st.columns([1, 0.1])

            with col1:
                st.markdown(f"""
                <div class="file-item" data-file-id="{file_id}">
                    <div class="file-name">{filename}</div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                if st.button("🗑️", key=f"delete_{file_id}", help="Удалить файл"):
                    try:
                        api = Api()
                        api.delete_file(file_id)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Ошибка при удалении: {str(e)}")
    else:
        st.markdown('<div class="no-files">Нет загруженных файлов</div>', unsafe_allow_html=True)

    st.markdown("""
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
