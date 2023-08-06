# Weather Forecast App

This is a machine learning weather forecast web app built with Streamlit for Indian cities.

## Overview

The app trains a random forest regression model on historical weather data to predict precipitation. It provides location-specific forecasts by taking in temperature, humidity and pressure inputs. The model is customized for major Indian cities.

Real-time weather forecasts are incorporated using the India Meteorological Department (IMD) API. 

## Usage
The app can be run with:
```
streamlit run main.py
```

Requirements:

- streamlit  
- pandas
- scikit-learn
- imdapy

An IMD developer account and API key is needed to access the weather forecasts.

## Data 

The model is trained on `india_weather_data.csv` which contains historical weather measurements for major Indian cities. Additional location-specific data can be added to this CSV to improve model accuracy.

## Customization

The app can be customized by:

- Adding more cities in the location dropdown
- Tuning the ML model parameters and algorithms
- Adding additional weather features like wind speed  
- Integrating forecasts from other weather API providers

## License

This project is open source and available under the [MIT License](LICENSE).

Let me know if you would like any changes or have additional questions!
