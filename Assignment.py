)## Packages
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

## Retrieve weather data
if a == WeatherData:

    key = st.text_input('Enter your OpenWeather API key:')
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid={key}'

    submit = st.button('Retrieve Weather data')

    if submit:
        st.write('Weather data is being retrieved.')

        response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()

            weather_df = pd.DataFrame(weather_data)

            # Format the temperature column to Celsius
            weather_df['main.temp'] = weather_df['main.temp'] - 273.15

            # Display the DataFrame in Streamlit
            st.dataframe(weather_df)
        else:
            st.error(f"Error retrieving weather data: {response.status_code}")
    else: st.error('Hello')



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