import streamlit as st
from src.components import header
from src.components import sidebar


def render_demo_content():
    st.markdown(f"""
    <div class="demo-main-content">

    </div>
    """, unsafe_allow_html=True)

def render_demo_page():
    header.render_page_header()
    sidebar.render_sidebar()
    render_demo_content()
