#from fastapi import FastAPI
import httpx, uvicorn
#from pydantic import BaseModel


from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
import httpx  # For making HTTP requests
from typing import Dict

app = FastAPI()


# Replace with your Meteomatics API credentials
METEOMATICS_USERNAME = "googlecloud_matosferreira_andr"
METEOMATICS_PASSWORD = "24VtfZF67k"
METEOMATICS_BASE_URL = "https://api.meteomatics.com/2024-01-01T00:00:00Z/t_2m:C/latitude,longitude/json"

async def get_weather_data(latitude: float, longitude: float) -> Dict:
    """Fetches weather data from the Meteomatics API."""
    url = METEOMATICS_BASE_URL.replace("latitude", str(latitude)).replace("longitude", str(longitude))
    auth = httpx.BasicAuth(METEOMATICS_USERNAME, METEOMATICS_PASSWORD)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, auth=auth)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error connecting to Meteomatics API: {e}")

@app.put("/weather/{latitude},{longitude}")
async def get_current_weather(latitude: float, longitude: float):
    """FastAPI endpoint to get weather data for a given location."""

    weather_data = await get_weather_data(latitude, longitude)
    return JSONResponse(content=weather_data)


if __name__ == '__main__':
    uvicorn.run(app, host = '0.0.0.0', port=8000, reload=True)






    