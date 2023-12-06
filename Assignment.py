## Packages
import streamlit as st
import pandas as pd
import numpy as np
!pip install matplotlib
import matplotlib.pyplot as plt

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
    file = st.file_uploader("Upload your data:", type=["csv"])

if a == Test2:

    x = np.linspace(0, 10, 200) 
    y = 2 * x + 1 + np.random.normal(0, 2, size=len(x))

    # Plot the dataset
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data points')
    ax.plot(x, 2 * x + 1, color='red', linestyle='--', label='True line')
    ax.set_title('Generated Dataset with Noise')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()

    st.pyplot(fig)