import base64
from pathlib import Path
import streamlit as st
from src.components import header
from src.utils import load_icon

def render():
    header.render_page_header()

    arrow_icon = load_icon("src/assets/icons/arrow-down.svg", 24, 24)
    hand_icon = load_icon("src/assets/icons/by-hand.svg", 48, 48)
    shield_icon = load_icon("src/assets/icons/shield.svg", 48, 48)
    speed_icon = load_icon("src/assets/icons/speed.svg", 48, 48)
    flow_image = load_icon("src/assets/images/flow.svg", 500, 300)
    arrow_right_icon = load_icon("src/assets/icons/arrow-right.svg", 24, 24)

    st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

      .header-info, .header-info * { font-family: 'Montserrat', sans-serif; }

      .header-info {
        width: 100%;
        margin-top: 130px;
        text-align: start;
        gap:100px;
        display: flex;
        flex-direction: column;
      }

      .header-slogan {
        font-size: 15px;
        color: #6D4BC4;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        display: inline-block;
        margin-bottom: 8px;
      }

      .section-title {
        font-size: 45px;
        color: #FFFFFF;
        font-weight: 700;
        line-height: 1.15;
        display: block;
        margin-bottom: 18px;
        margin: 0;
      }

      .header-title {
        margin: 0 auto;
        width: 520px;
      }

      .feature-p {
        text-transform: uppercase;
        color: #FFFFFF;
        font-size: 15px !important;
      }

      .outline-button {
        padding: 11px 17px;
        border: 1px solid transparent;
        background:
          linear-gradient(transparent, transparent) padding-box,
          linear-gradient(90deg, #9588D4 47%, #4D476E 100%) border-box;
        -webkit-background-clip: padding-box, border-box;
        background-clip: padding-box, border-box;
        background-color: transparent;
        border-radius: 10px;
        color: #fff;
      }

      .button {
        padding: 11px 17px;
        border: 1px solid transparent;
        width:fit-content;
        background:
          linear-gradient(#6D4BC4, #6D4BC4) padding-box,
          linear-gradient(90deg, #9588D4 47%, #4D476E 100%) border-box;
        -webkit-background-clip: padding-box, border-box;
        background-clip: padding-box, border-box;
        border-radius: 10px;
        color: #fff;
      }

        .outline-button {
              padding: 11px 17px;
                border: 1px solid transparent;
                background:
                  linear-gradient(#0A0A0A, #0A0A0A) padding-box,
                  linear-gradient(90deg, #9588D4 47%, #4D476E 100%) border-box;
                -webkit-background-clip: padding-box, border-box;
                background-clip: padding-box, border-box;
                -webkit-text-fill-color: initial;
              border-radius: 10px;
          }

      .feature-right-part , .feature-left-part {
        padding: 25px  30px;
      }

      .feature-left-part {
        text-align: end;
      }


      .feature-right-part {
        display:flex;
        flex-direction: column;
        border-left: 2px solid #222222;
        gap: 20px;
      }
      .header-feature {
        display: grid;
        grid-template-columns: 1fr 850px;
        border-top: 2px solid #222222;
      }

      .feature-buttons {
        display:flex;
        gap: 16px;
      }

      .tasks-section {
        display: flex;
        flex-direction: column;
        gap:45px ;
      }

      .tasks-container {
        display: grid;
        gap: 28px;
        grid-template-columns: repeat(3, 1fr)
      }

      .task-card {
         display:flex;
         flex-direction: column;
         justify-content: space-between;
         max-width: 400px;
         width:100%;
         height:100%;
         height: 505px;
         border: 1px solid #18171C;
         border-radius: 20px;
         padding: 34px
      }

      .card-name {
            font-size: 12px;
            display: flex;
            justify-content: end;
            align-items: center;
            color: #605395;
      }

      .card-info {
          display: flex;
          flex-direction: column;
          gap: 16px;
          padding:34px
          align-items:start;
          justify-content: center;
      }

      .card-title {
        font-size: 21px;
        font-weight: 400;
        color:#FFFFFF;
      }

      .p-desc {
         font-size: 14px;
         color: #D8D8D8;
         margin: 0;
      }

      .solution-section {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 56px;
      }

      .solution-right {
      display: flex;
      flex-direction: column;
      gap:36px;
      }

      .feature-list {
        display: flex;
        flex-direction: column;
        gap: 7px;
      }

      .feature-item {
        display:flex;
        justify-content:start;
        align-items: center;
      }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="header-info">
      <div class="header-title">
        <span class="header-slogan">[ Слоган ]</span>
        <span class="section-title">
          Сложные контракты<br/>Простые решения
        </span>
      </div>

      <div class="header-feature">
        <div class="feature-left-part">
            <p class="feature-p">
            { arrow_icon}
             Узнай больше
             <p/>
        </div>
        <div class="feature-right-part">
          <p class="feature-p">
            Наш AI-ассистент автоматизирует аудит валютных контрактов, сокращает время проверки с 30 минут до 2 минут и снижает риски. Мы превращаем рутину в быстрые и точные решения.
          </p>
          <div class="feature-buttons">
            <button class="button">Попробовать демо</button>
            <button class="outline-button">Узнать больше</button>
          </div>
        </div>
      </div>

      <div class="tasks-section">
            <span class="section-title">Задачи</span>
            <div class="tasks-container">
                <div class="task-card">
                    <span class="card-name">[ Блок 1 ]</span>
                    <div class="card-info">
                        { hand_icon }
                        <span class="card-title">
                            От ручной проверки к автоматизации
                        </span>
                        <p class="p-desc">
                            AI извлекает данные из валютных договоров и автоматически формирует отчёт, избавляя сотрудников от рутинной работы.
                        </p>
                    </div>
                </div>
               <div class="task-card">
                 <span class="card-name">[ Блок 2 ]</span>
                 <div class="card-info">
                   {shield_icon}
                   <span class="card-title">Снижение рисков и ошибок</span>
                   <p class="p-desc">
                     Система выявляет нарушения и проверяет соответствие требованиям,
                     уменьшая вероятность штрафов и санкций.
                   </p>
                 </div>
               </div>
               <div class="task-card">
                 <span class="card-name">[ Блок 3 ]</span>
                 <div class="card-info">
                   {speed_icon}
                   <span class="card-title">Скорость и эффективность</span>
                   <p class="p-desc">
                     Проверка валютного контракта занимает не 30 минут, а всего 2 —
                     больше сделок за меньшее время.
                   </p>
                 </div>
               </div>
            </div>
      </div>
      <div class="solution-section">
            <div class="solution-left">
                {flow_image}
            </div>
            <div class="solution-right">
                <span class="header-slogan">[ Наше решение ]</span>
                <span class="section-title">
                    AI-ассистент валютного контроля
                </span>
                <p class="p-desc">
                    Мы разработали AI-систему, которая берёт на себя аудит валютных договоров: извлекает данные из документов, проверяет на нарушения и формирует готовый отчёт. Это снижает риски, экономит время и усиливает контроль.
                </p>
                <div class="features-list">
                    <div class="feature-item">
                        {arrow_right_icon}
                        <p class="p-desc">Проверка договора за 2 минуты вместо 30</p>
                    </div>
                    <div class="feature-item">
                       {arrow_right_icon}
                       <p class="p-desc">Автоматическое извлечение данных из документов</p>
                    </div>
                    <div class="feature-item">
                       {arrow_right_icon}
                       <p class="p-desc"> Проверка на нарушения и санкционный комплаенс</p>
                    </div>
                    <div class="feature-item">
                       {arrow_right_icon}
                       <p class="p-desc"> Готовый отчёт для сотрудника</p>
                    </div>
                </div>
                <button class="button">Попробовать демо</button>
            </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
