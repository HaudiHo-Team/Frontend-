import streamlit as st
import streamlit.components.v1 as components
import json

def render_field_annotation(file_data, filename, coordinates=None):
    """Компонент для отметки полей на документе"""
    
    st.markdown("""
    <style>
    .annotation-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        border: none;
        padding: 20px;
        margin: 20px 0;
    }
    
    .annotation-title {
        font-size: 20px;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 16px;
        text-align: center;
    }
    
    .document-canvas {
        width: 100%;
        height: 600px;
        border: none;
        border-radius: 12px;
        background: #FFFFFF;
        position: relative;
        overflow: hidden;
    }
    
    .field-list {
        margin-top: 16px;
        padding: 12px;
        background: rgba(149, 136, 212, 0.1);
        border-radius: 8px;
        border: none;
    }
    
    .field-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px;
        margin: 4px 0;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .field-item:hover {
        background: rgba(149, 136, 212, 0.2);
    }
    
    .field-checkbox {
        width: 16px;
        height: 16px;
    }
    
    .field-label {
        font-size: 14px;
        color: #D8D8D8;
        flex: 1;
    }
    
    .field-coordinates {
        font-size: 12px;
        color: #9588D4;
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Список полей для отметки
    fields = [
        {"id": "contract_number", "label": "Номер контракта", "icon": "📄"},
        {"id": "contract_start_date", "label": "Дата заключения", "icon": "📅"},
        {"id": "contract_end_date", "label": "Дата окончания", "icon": "📅"},
        {"id": "counterparty", "label": "Контрагент", "icon": "🏢"},
        {"id": "country", "label": "Страна", "icon": "🌍"},
        {"id": "contract_amount", "label": "Сумма контракта", "icon": "💰"},
        {"id": "contract_currency", "label": "Валюта контракта", "icon": "💱"},
        {"id": "payment_currency", "label": "Валюта платежа", "icon": "💳"}
    ]
    
    # HTML для интерактивного отображения документа
    annotation_html = f"""
    <div class="annotation-container">
        <div class="annotation-title">📝 Отметка полей на документе</div>
        
        <canvas id="annotationCanvas" class="document-canvas" width="800" height="600"></canvas>
        
        <div class="field-list">
            <h4 style="color: #9588D4; margin-bottom: 12px;">Поля для отметки:</h4>
            {''.join([f'''
            <div class="field-item" data-field="{field['id']}">
                <input type="checkbox" class="field-checkbox" id="field_{field['id']}">
                <span class="field-label">{field['icon']} {field['label']}</span>
                <span class="field-coordinates" id="coords_{field['id']}">Не отмечено</span>
            </div>
            ''' for field in fields])}
        </div>
    </div>
    
    <script>
    // Получаем canvas и контекст
    const canvas = document.getElementById('annotationCanvas');
    const ctx = canvas.getContext('2d');
    
    // Координаты с бэкенда
    const coordinates = {json.dumps(coordinates or [])};
    
    // Состояние отмеченных полей
    const markedFields = {{}};
    
    // Функция для рисования документа
    function drawDocument() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Рисуем фон документа (имитация)
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Рисуем линии по координатам
        if (coordinates && coordinates.length > 0) {{
            ctx.strokeStyle = '#9588D4';
            ctx.lineWidth = 2;
            ctx.lineCap = 'round';
            
            coordinates.forEach((line, index) => {{
                if (line && line.length >= 2) {{
                    ctx.beginPath();
                    ctx.moveTo(line[0].x, line[0].y);
                    
                    for (let i = 1; i < line.length; i++) {{
                        ctx.lineTo(line[i].x, line[i].y);
                    }}
                    
                    ctx.stroke();
                }}
            }});
        }}
        
        // Рисуем отмеченные поля
        Object.values(markedFields).forEach(field => {{
            if (field.coordinates) {{
                ctx.fillStyle = 'rgba(149, 136, 212, 0.3)';
                ctx.fillRect(field.coordinates.x - 5, field.coordinates.y - 5, 10, 10);
                
                ctx.fillStyle = '#9588D4';
                ctx.font = '12px Arial';
                ctx.fillText(field.label, field.coordinates.x + 15, field.coordinates.y + 5);
            }}
        }});
    }}
    
    // Обработка клика по canvas
    canvas.addEventListener('click', function(e) {{
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        // Находим активное поле
        const activeField = document.querySelector('.field-item.active');
        if (activeField) {{
            const fieldId = activeField.dataset.field;
            const fieldLabel = activeField.querySelector('.field-label').textContent;
            
            // Сохраняем координаты
            markedFields[fieldId] = {{
                label: fieldLabel,
                coordinates: {{x: x, y: y}}
            }};
            
            // Обновляем отображение
            activeField.querySelector('.field-coordinates').textContent = `(${{x}}, ${{y}})`;
            activeField.classList.remove('active');
            
            drawDocument();
        }}
    }});
    
    // Обработка клика по полям
    document.querySelectorAll('.field-item').forEach(item => {{
        item.addEventListener('click', function(e) {{
            if (e.target.type !== 'checkbox') {{
                // Убираем активность с других полей
                document.querySelectorAll('.field-item').forEach(i => i.classList.remove('active'));
                
                // Активируем текущее поле
                this.classList.add('active');
                
                // Показываем инструкцию
                canvas.style.cursor = 'crosshair';
            }}
        }});
    }});
    
    // Обработка чекбоксов
    document.querySelectorAll('.field-checkbox').forEach(checkbox => {{
        checkbox.addEventListener('change', function() {{
            const fieldId = this.id.replace('field_', '');
            const fieldItem = this.closest('.field-item');
            
            if (this.checked) {{
                fieldItem.classList.add('active');
                canvas.style.cursor = 'crosshair';
            }} else {{
                fieldItem.classList.remove('active');
                canvas.style.cursor = 'default';
                
                // Удаляем координаты
                delete markedFields[fieldId];
                fieldItem.querySelector('.field-coordinates').textContent = 'Не отмечено';
                drawDocument();
            }}
        }});
    }});
    
    // Инициализация
    drawDocument();
    
    // Обработка изменения размера canvas
    function resizeCanvas() {{
        const container = canvas.parentElement;
        canvas.width = container.clientWidth - 4;
        canvas.height = 600;
        drawDocument();
    }}
    
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    </script>
    """
    
    components.html(annotation_html, height=800)

def render_simple_field_list():
    """Простой список полей для отметки"""
    
    st.markdown("### 📝 Поля для отметки")
    
    fields = [
        ("📄", "Номер контракта", "contract_number"),
        ("📅", "Дата заключения", "contract_start_date"),
        ("📅", "Дата окончания", "contract_end_date"),
        ("🏢", "Контрагент", "counterparty"),
        ("🌍", "Страна", "country"),
        ("💰", "Сумма контракта", "contract_amount"),
        ("💱", "Валюта контракта", "contract_currency"),
        ("💳", "Валюта платежа", "payment_currency")
    ]
    
    for icon, label, field_id in fields:
        col1, col2 = st.columns([1, 4])
        with col1:
            checked = st.checkbox("", key=f"field_{field_id}")
        with col2:
            st.write(f"{icon} {label}")
    
    if st.button("💾 Сохранить отметки", type="primary"):
        st.success("Отметки сохранены!")
