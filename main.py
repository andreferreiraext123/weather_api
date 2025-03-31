from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx
from typing import Dict, Any
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup  # Importe BeautifulSoup
#import database



app = FastAPI()

load_dotenv()
METEOMATICS_USERNAME = os.getenv("METEOMATICS_USERNAME")
METEOMATICS_PASSWORD = os.getenv("METEOMATICS_PASSWORD")

METEOMATICS_BASE_URL = "https://api.meteomatics.com/{time}/t_2m:C/{latitude},{longitude}/json"  # Corrigido para /json

async def get_weather_data(latitude: float, longitude: float, time: str) -> Dict[str, Any]:  # Adicionado parâmetro time
    """Fetches weather data from the Meteomatics API."""
    url = METEOMATICS_BASE_URL.format(time=time, latitude=latitude, longitude=longitude)
    auth = httpx.BasicAuth(METEOMATICS_USERNAME, METEOMATICS_PASSWORD)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, auth=auth)
            response.raise_for_status()
            return response.json()  # Retorna JSON
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error connecting to Meteomatics API: {e}")

@app.get("/weather/{latitude},{longitude}/{time}")  # Rota com parâmetro time
async def get_current_weather(latitude: float, longitude: float, time: str):  # Função com parâmetro time
    """FastAPI endpoint to get weather data for a given location."""

    # Validate latitude and longitude
    if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
        raise HTTPException(status_code=400, detail="Invalid latitude or longitude.")

    weather_data = await get_weather_data(latitude, longitude, time)  # Chame a função com o parâmetro time
    return JSONResponse(content=weather_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)