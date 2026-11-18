# design.py
import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .main-header { font-size: 2.8rem; font-weight: 800; margin-bottom: 0px; padding-bottom: 0px;}
        .sub-header { font-size: 1.2rem; color: #888888; margin-top: 0px; padding-top: 0px; margin-bottom: 2rem;}
        .stTabs [data-baseweb="tab-list"] { gap: 2rem; }
        .stTabs [data-baseweb="tab"] { font-size: 1.1rem; font-weight: 600; }
        </style>
    """, unsafe_allow_html=True)

def render_hero():
    st.markdown('<p class="main-header">Gui Shi Jun</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Interactive Game Development | AR/VR Engineer | iOS & Full-Stack</p>', unsafe_allow_html=True)
    st.write("Welcome to my live Digital Twin. This portfolio is autonomously maintained by a custom Python Discord bot connected to a Supabase cloud vault.")
    st.divider()