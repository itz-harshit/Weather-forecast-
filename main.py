# Made by https://me.harshit.wtf
# Import libraries
#Note : Create a file named "india_weather_data.csv" before using 
import streamlit as st
from imdapy import IMD
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# Load model
df = pd.read_csv('india_weather_data.csv')
X = df[['temperature', 'humidity', 'pressure']]
y = df['precipitation']

model = RandomForestRegressor()
model.fit(X, y)

# API credentials
imd = IMD(api_key)

# Get forecast data 
city = "Delhi"
forecast = imd.get_forecast(city=city, product="three_hour")  

temp = forecast['temp']
humidity = forecast['humidity']
pressure = forecast['pressure']

# Make prediction
data = [[temp, humidity, pressure]]
prediction = model.predict(data)

# Display  
st.title("Weather Forecast for "+city)
st.write("IMD Forecast:", forecast['precipitation'])
st.write("Predicted Precipitation:", prediction[0])
