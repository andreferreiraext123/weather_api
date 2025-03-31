from typing import Dict, Any, Optional, List, Union
from fastapi import HTTPException
import httpx
import os
from dotenv import load_dotenv


load_dotenv()
METEOMATICS_USERNAME = os.getenv("METEOMATICS_USERNAME")
METEOMATICS_PASSWORD = os.getenv("METEOMATICS_PASSWORD")
METEOMATICS_BASE_URL = "https://api.meteomatics.com/{time}/{parameters}/{coordinates}/{format}"


async def get_weather_data(
    latitude: float,
    longitude: float,
    time: str,
    parameters: Union[str, List[str]],
    format: str = "json",
    altitude: Optional[float] = None,
    time_interval: Optional[str] = None,
    model: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Fetches weather data from the Meteomatics API.

    Args:
        latitude: Latitude of the location.
        longitude: Longitude of the location.
        time: The time or time range for the data request.
        parameters: A single parameter or a list of parameters to retrieve.
        format: The desired format of the response (e.g., 'json', 'csv').
        altitude: (Optional) Altitude of the location.
        time_interval: (Optional) The time interval for the data.
        model: (Optional) Which model to use.

    Returns:
        A dictionary containing the weather data.

    Raises:
        HTTPException: If there's an error connecting to the API.
    """

    coordinates = f"{latitude},{longitude}"
    url = f"https://api.meteomatics.com/{time}/{','.join(parameters) if isinstance(parameters, list) else parameters}/{coordinates}/{format}"

    # Add options to the URL
    if altitude is not None:
        url += f":{altitude}"
    if time_interval is not None:
        url = url.replace(time, f"{time}:{time_interval}")
    if model is not None:
        url += f"?model={model}"

    auth = httpx.BasicAuth(METEOMATICS_USERNAME, METEOMATICS_PASSWORD)

    async with httpx.AsyncClient() as client:
        try:
            print(f"Request URL: {url}")
            response = await client.get(url, auth=auth)
            response.raise_for_status()

            if format == "json":
                return response.json()
            elif format == "csv":
                return {"csv_data": response.text}
            elif format == "html":
                return {"html_data": response.text}
            else:
                return {"raw_data": response.text}

        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error connecting to Meteomatics API: {e}")