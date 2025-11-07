from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Accurate Weather API ", version="1.0")

WEATHER_API_KEY = os.getenv("WEATHERAPI_KEY")
POSTAL_API_URL = "https://api.postalpincode.in/pincode/"
WEATHER_URL = "https://api.weatherapi.com/v1/current.json"


class WeatherResponse(BaseModel):
    location: str
    temperature_celsius: float
    humidity: int
    weather_description: str
    pressure: float


@app.get("/weather", response_model=WeatherResponse)
async def get_weather(location: str):
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="Missing WEATHERAPI_KEY in .env")

    async with httpx.AsyncClient() as client:

        if location.isdigit():
            postal_response = await client.get(POSTAL_API_URL + location)
            postal_data = postal_response.json()

            if not postal_data or postal_data[0]["Status"] != "Success":
                raise HTTPException(status_code=404, detail="Invalid or unsupported pincode")

            city = postal_data[0]["PostOffice"][0]["District"]
        else:
            city = location

        weather_params = {"key": WEATHER_API_KEY, "q": city}
        weather_response = await client.get(WEATHER_URL, params=weather_params)

        if weather_response.status_code != 200:
            raise HTTPException(status_code=404, detail="Weather data not found")

        data = weather_response.json()

    return WeatherResponse(
        location=f"{data['location']['name']}, {data['location']['region']}, {data['location']['country']}",
        temperature_celsius=data["current"]["temp_c"],
        humidity=data["current"]["humidity"],
        weather_description=data["current"]["condition"]["text"],
        pressure=data["current"]["pressure_mb"]
    )
