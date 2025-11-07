# Weather API (FastAPI + WeatherAPI.com)

This project provides a simple **GET API** that returns **current weather details** for a given **City Name** or **Indian Pincode**.  
It uses external public APIs to retrieve accurate weather and location data.

---

## Features

-   Accepts **city name** or **Indian pincode**
-   Automatically **detects pincode** and resolves it to the correct district using Government of India Postal API
-   Retrieves **current weather data** from **WeatherAPI.com**
-   Returns clean weather info:
    -   Location (City, State/Region, Country)
    -   Temperature (°C)
    -   Humidity (%)
    -   Weather Condition Text
    -   Atmospheric Pressure (mb)
-   Built with **FastAPI** (lightweight and fast)

---

## API Endpoints

| Method | Endpoint   | Description                    |
| ------ | ---------- | ------------------------------ |
| GET    | `/weather` | Get weather by city or pincode |

## Requirements

-   Python 3.12
-   WeatherAPI.com API key (free): https://www.weatherapi.com/

## run project

pip install requirement.txt
uvicorn main:app --reload

## Swagger

http://127.0.0.1:8000/docs

## Sample Response

```json
{
    "location": "Chennai, Tamil Nadu, India",
    "temperature_celsius": 31.2,
    "humidity": 75,
    "weather_description": "Mist",
    "pressure": 1008
}
```
