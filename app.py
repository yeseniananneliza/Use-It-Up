"""Use It Up: serves the recipe site (index.html) through Streamlit.

The whole app lives in index.html (plain HTML, CSS and JavaScript), so the
same file also runs on GitHub Pages. This wrapper keeps the original
use-it-up.streamlit.app link working.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Use It Up", page_icon="🍳", layout="wide")

# Hide Streamlit's own chrome so only the site shows, full screen.
st.markdown(
    """
    <style>
    header[data-testid="stHeader"], #MainMenu, footer,
    [data-testid="stToolbar"], [data-testid="stDecoration"] {display: none !important;}
    .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important; max-width: 100% !important;
    }
    [data-testid="stVerticalBlock"] {gap: 0 !important;}
    iframe {display: block; width: 100%; height: 100vh !important; border: 0;}
    .stApp {overflow: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
