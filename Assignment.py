import streamlit as st


st.set_page_config(
    page_title="Sentiment-Analyse",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",    
)

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        right: 0;
        font-size: 12px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="footer">© 2023 Capstone Gruppe Research. All rights reserved.</div>',
    unsafe_allow_html=True,
)