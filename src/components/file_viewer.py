import streamlit as st
import streamlit.components.v1 as components
import json
import base64
import io

def render_file_viewer(file_data=None, coordinates=None):
    """Отображает файл с возможностью рисования линий по координатам"""
    
    if not file_data:
        return
    
    st.markdown("""
    <style>
    .file-viewer-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin: 20px 0;
        position: relative;
        overflow: hidden;
    }
    
    .file-viewer-title {
        font-size: 20px;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 16px;
        text-align: center;
    }
    
    .file-canvas {
        width: 100%;
        height: 600px;
        border: 2px solid rgba(149, 136, 212, 0.3);
        border-radius: 12px;
        background: #FFFFFF;
        position: relative;
        overflow: hidden;
    }
    
    .coordinates-info {
        margin-top: 16px;
        padding: 12px;
        background: rgba(149, 136, 212, 0.1);
        border-radius: 8px;
        border: 1px solid rgba(149, 136, 212, 0.2);
    }
    
    .coordinates-title {
        font-size: 14px;
        font-weight: 600;
        color: #9588D4;
        margin-bottom: 8px;
    }
    
    .coordinates-list {
        font-size: 12px;
        color: #D8D8D8;
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # HTML для отображения файла с canvas
    file_viewer_html = f"""
    <div class="file-viewer-container">
        <div class="file-viewer-title">📄 Просмотр документа</div>
        <canvas id="fileCanvas" class="file-canvas" width="800" height="600"></canvas>
        <div class="coordinates-info">
            <div class="coordinates-title">Координаты линий:</div>
            <div class="coordinates-list" id="coordinatesList">Загрузка...</div>
        </div>
    </div>
    
    <script>
    // Получаем canvas и контекст
    const canvas = document.getElementById('fileCanvas');
    const ctx = canvas.getContext('2d');
    const coordinatesList = document.getElementById('coordinatesList');
    
    // Координаты с бэкенда
    const coordinates = {json.dumps(coordinates or [])};
    
    // Функция для рисования линий
    function drawLines() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Настройки для линий
        ctx.strokeStyle = '#9588D4';
        ctx.lineWidth = 2;
        ctx.lineCap = 'round';
        
        // Рисуем линии по координатам
        coordinates.forEach((line, index) => {{
            if (line && line.length >= 2) {{
                ctx.beginPath();
                ctx.moveTo(line[0].x, line[0].y);
                
                for (let i = 1; i < line.length; i++) {{
                    ctx.lineTo(line[i].x, line[i].y);
                }}
                
                ctx.stroke();
                
                // Добавляем номер линии
                if (line[0]) {{
                    ctx.fillStyle = '#9588D4';
                    ctx.font = '12px Arial';
                    ctx.fillText((index + 1).toString(), line[0].x + 5, line[0].y - 5);
                }}
            }}
        }});
        
        // Обновляем информацию о координатах
        updateCoordinatesInfo();
    }}
    
    // Функция для обновления информации о координатах
    function updateCoordinatesInfo() {{
        let info = '';
        coordinates.forEach((line, index) => {{
            if (line && line.length > 0) {{
                info += `Линия ${{index + 1}}: `;
                line.forEach((point, pointIndex) => {{
                    info += `(${{point.x}}, ${{point.y}})`;
                    if (pointIndex < line.length - 1) info += ' → ';
                }});
                info += '<br>';
            }}
        }});
        
        if (info === '') {{
            info = 'Нет координат для отображения';
        }}
        
        coordinatesList.innerHTML = info;
    }}
    
    // Загружаем изображение файла (если есть)
    function loadFileImage() {{
        // Здесь можно добавить загрузку изображения файла
        // const img = new Image();
        // img.onload = function() {{
        //     ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
        //     drawLines();
        // }};
        // img.src = 'path/to/file/image';
        
        // Пока просто рисуем линии
        drawLines();
    }}
    
    // Инициализация
    loadFileImage();
    
    // Обработка изменения размера canvas
    function resizeCanvas() {{
        const container = canvas.parentElement;
        canvas.width = container.clientWidth - 4; // учитываем border
        canvas.height = 600;
        drawLines();
    }}
    
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    </script>
    """
    
    components.html(file_viewer_html, height=700)

def render_coordinates_table(coordinates=None):
    """Отображает таблицу с координатами"""
    
    if not coordinates:
        st.info("Нет координат для отображения")
        return
    
    st.markdown("### 📊 Координаты линий")
    
    # Создаем DataFrame для отображения координат
    import pandas as pd
    
    data = []
    for i, line in enumerate(coordinates):
        if line and len(line) > 0:
            for j, point in enumerate(line):
                data.append({
                    'Линия': i + 1,
                    'Точка': j + 1,
                    'X': point.get('x', 0),
                    'Y': point.get('y', 0)
                })
    
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Координаты не найдены")

def render_pdf_viewer(file_data, filename):
    """Отображает PDF файл для чтения"""
    
    try:
        # Кодируем PDF в base64 для отображения
        pdf_base64 = base64.b64encode(file_data).decode('utf-8')
        
        # HTML для отображения PDF
        pdf_html = f"""
        <div style="width: 100%; height: 600px; border: 2px solid rgba(149, 136, 212, 0.3); border-radius: 12px; overflow: hidden;">
            <iframe 
                src="data:application/pdf;base64,{pdf_base64}" 
                width="100%" 
                height="100%" 
                style="border: none;"
                type="application/pdf">
            </iframe>
        </div>
        """
        
        st.markdown("### 📄 Просмотр документа")
        components.html(pdf_html, height=600)
        
    except Exception as e:
        st.error(f"Ошибка при отображении PDF: {str(e)}")
        # Fallback - показываем информацию о файле
        st.info(f"Файл: {filename} (PDF не может быть отображен)")

def render_simple_file_display(filename, coordinates=None, file_data=None):
    """Простое отображение файла с линиями"""
    
    st.markdown("""
    <style>
    .simple-file-display {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin: 16px 0;
    }
    
    .file-name {
        font-size: 18px;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 16px;
        text-align: center;
    }
    
    .coordinates-summary {
        background: rgba(149, 136, 212, 0.1);
        border-radius: 8px;
        padding: 12px;
        margin-top: 12px;
    }
    
    .summary-title {
        font-size: 14px;
        font-weight: 600;
        color: #9588D4;
        margin-bottom: 8px;
    }
    
    .summary-text {
        font-size: 12px;
        color: #D8D8D8;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Подсчитываем статистику
    total_lines = len(coordinates) if coordinates else 0
    total_points = sum(len(line) for line in coordinates) if coordinates else 0
    
    st.markdown(f"""
    <div class="simple-file-display">
        <div class="file-name">📄 {filename}</div>
        <div class="coordinates-summary">
            <div class="summary-title">Статистика координат:</div>
            <div class="summary-text">
                Линий: {total_lines}<br>
                Точек: {total_points}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Если есть данные файла и это PDF, показываем его
    if file_data and filename.lower().endswith('.pdf'):
        render_pdf_viewer(file_data, filename)
    
    # Показываем координаты в виде JSON
    if coordinates:
        with st.expander("🔍 Детальные координаты"):
            st.json(coordinates)
