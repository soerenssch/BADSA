## Packages
import streamlit as st
import pandas as pd
import numpy as np
import requests
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
WeatherData = 'Weather Data'
Visualisation = 'Visualisation'

a = st.sidebar.radio('Choose:',[WeatherData, Visualisation])

## Upload data to analyse
if a == WeatherData:
    file = st.file_uploader("Upload your data:", type=["csv"])


    key = st.text_input('Enter your OpenWeather API key:')
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid={key}'

    response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()

        # Print current weather conditions
        st.write(f"Current weather conditions for London:")
        st.write("------------------------------------")
        st.write(f"Temperature: {weather_data['main']['temp']}°C")
        st.write(f"Humidity: {weather_data['main']['humidity']:.0f}%")
        st.write(f"Pressure: {weather_data['main']['pressure']} hPa")
        st.write(f"Description: {weather_data['weather'][0]['description']}")
    else:
        st.error(f"Error retrieving weather data: {response.status_code}")



if a == Visualisation:

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