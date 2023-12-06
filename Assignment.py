## Packages
import streamlit as st
import pandas as pd

## Graphic layout streamlit
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
    '<div class="footer">© 2023 Business Analytics and Data Science Applications. All rights reserved.</div>',
    unsafe_allow_html=True,
)

st.header('Hello')

## Sidebar
UploadData = 'Upload data'
Test2 = 'Test2'

a = st.sidebar.radio('Choose:',[UploadData, Test2])

## Upload data to analyse
if a == UploadData:
    file = st.file_uploader("Laden Sie Ihre Datei hier hoch:", type=["csv"])

