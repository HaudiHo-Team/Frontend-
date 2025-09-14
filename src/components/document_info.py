import streamlit as st
from typing import Dict, Any, Optional

def render_document_info(document_data: Optional[Dict[str, Any]] = None):
    """Отображает информацию о документе с красивым дизайном"""
    
    if not document_data:
        return
    
    st.markdown("""
    <style>
    .document-info {
        background: linear-gradient(135deg, rgba(149, 136, 212, 0.1) 0%, rgba(77, 71, 110, 0.1) 100%);
        border-radius: 16px;
        padding: 32px;
        border: 1px solid rgba(149, 136, 212, 0.2);
        margin-top: 24px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .document-title {
        font-size: 28px;
        font-weight: 700;
        color: #FFFFFF;
        margin: 0 0 24px 0;
        text-align: center;
        padding-bottom: 20px;
        border-bottom: 2px solid rgba(149, 136, 212, 0.3);
        background: linear-gradient(90deg, #9588D4 0%, #FFFFFF 50%, #9588D4 100%);
        background-size: 200% 100%;
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s ease-in-out infinite;
    }
    
    @keyframes shimmer {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    
    .document-field {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 20px;
        margin: 8px 0;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .document-field::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(149, 136, 212, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .document-field:hover {
        transform: translateX(4px);
        background: rgba(149, 136, 212, 0.1);
        border-color: rgba(149, 136, 212, 0.3);
        box-shadow: 0 4px 16px rgba(149, 136, 212, 0.2);
    }
    
    .document-field:hover::before {
        left: 100%;
    }
    
    .field-label {
        font-size: 16px;
        color: #D8D8D8;
        font-weight: 600;
        min-width: 200px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .field-icon {
        width: 20px;
        height: 20px;
        opacity: 0.7;
    }
    
    .field-value {
        font-size: 16px;
        color: #FFFFFF;
        font-weight: 500;
        text-align: right;
        flex: 1;
        margin-left: 20px;
        padding: 8px 16px;
        background: rgba(149, 136, 212, 0.1);
        border-radius: 8px;
        border: 1px solid rgba(149, 136, 212, 0.2);
    }
    
    .loading-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 60px 20px;
        text-align: center;
    }
    
    .loading-spinner {
        width: 60px;
        height: 60px;
        border: 4px solid rgba(149, 136, 212, 0.2);
        border-top: 4px solid #9588D4;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-bottom: 24px;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .loading-text {
        font-size: 20px;
        color: #9588D4;
        font-weight: 600;
        margin-bottom: 12px;
    }
    
    .loading-subtext {
        font-size: 14px;
        color: #D8D8D8;
        opacity: 0.8;
    }
    
    .processing-dots {
        display: inline-block;
        animation: dots 1.5s infinite;
    }
    
    @keyframes dots {
        0%, 20% { content: ''; }
        40% { content: '.'; }
        60% { content: '..'; }
        80%, 100% { content: '...'; }
    }
    
    .success-message {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(22, 163, 74, 0.1) 100%);
        border: 1px solid rgba(34, 197, 94, 0.3);
        border-radius: 12px;
        padding: 16px 20px;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .success-text {
        color: #22C55E;
        font-weight: 600;
        font-size: 16px;
        margin: 0;
    }

    /* Адаптивность для мобильных устройств */
    @media (max-width: 768px) {
        .document-info {
            padding: 20px;
            margin-top: 16px;
        }
        
        .document-title {
            font-size: 24px;
            margin-bottom: 16px;
        }
        
        .document-field {
            flex-direction: column;
            align-items: flex-start;
            gap: 8px;
            padding: 12px 16px;
        }
        
        .field-label {
            min-width: auto;
            font-size: 14px;
        }
        
        .field-value {
            text-align: left;
            margin-left: 0;
            width: 100%;
            font-size: 14px;
        }
        
        .loading-container {
            padding: 40px 15px;
        }
        
        .loading-spinner {
            width: 50px;
            height: 50px;
        }
        
        .loading-text {
            font-size: 18px;
        }
    }

    @media (max-width: 480px) {
        .document-info {
            padding: 16px;
        }
        
        .document-title {
            font-size: 20px;
        }
        
        .document-field {
            padding: 10px 12px;
        }
        
        .field-label {
            font-size: 13px;
        }
        
        .field-value {
            font-size: 13px;
        }
        
        .loading-container {
            padding: 30px 10px;
        }
        
        .loading-spinner {
            width: 40px;
            height: 40px;
        }
        
        .loading-text {
            font-size: 16px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Если данные загружаются
    if document_data.get('loading', False):
        st.markdown("""
        <div class="document-info">
            <div class="loading-container">
                <div class="loading-spinner"></div>
                <div class="loading-text">Обработка документа<span class="processing-dots">...</span></div>
                <div class="loading-subtext">Нейронная сеть анализирует содержимое</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Отображение данных документа
    st.markdown("""
    <div class="document-info">
        <h2 class="document-title">📄 Информация о документе</h2>
    """, unsafe_allow_html=True)
    
    # Поля документа с иконками
    fields = [
        ("📄", "Номер контракта", document_data.get("contract_number", "—")),
        ("📅", "Дата заключения", document_data.get("contract_start_date", "—")),
        ("📅", "Дата окончания", document_data.get("contract_end_date", "—")),
        ("🏢", "Контрагент", document_data.get("counterparty", "—")),
        ("🌍", "Страна", document_data.get("country", "—")),
        ("💰", "Сумма контракта", document_data.get("contract_amount", "—")),
        ("💱", "Валюта контракта", document_data.get("contract_currency", "—")),
        ("💳", "Валюта платежа", document_data.get("payment_currency", "—"))
    ]
    
    for icon, label, value in fields:
        st.markdown(f"""
        <div class="document-field">
            <div class="field-label">
                <span class="field-icon">{icon}</span>
                {label}:
            </div>
            <div class="field-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
