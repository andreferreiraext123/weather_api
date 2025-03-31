from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict, Any
import uvicorn
from meteomatics_api import get_weather_data  # Importe a função do outro arquivo
from geolocations import estados  # Importe o dicionário do arquivo

app = FastAPI()


@app.get("/weather/{estado}/{cidade}/{time}")
async def get_current_weather(
    estado: str, cidade: str, time: str
) -> Dict[str, Any]:
    """
    FastAPI endpoint to get weather data by state and city.

    Args:
        estado: The name of the state.
        cidade: The name of the city.
        time: The time for the weather data.

    Returns:
        A dictionary containing the weather data.

    Raises:
        HTTPException: If the state or city is not found.
    """

    estado_corrigido = estado.lower()  # Force tudo para minúsculas
    cidade_corrigida = cidade.lower()  # Force tudo para minúsculas

    print(f"DEBUG: estado recebido = '{estado}'")
    print(f"DEBUG: cidade recebida = '{cidade}'")
    print(f"DEBUG: estado_corrigido = '{estado_corrigido}'")
    print(f"DEBUG: cidade_corrigida = '{cidade_corrigida}'")

    print(f"DEBUG: estado no dicionario = '{list(estados.keys())}'")
    if estado_corrigido not in estados:
        raise HTTPException(
            status_code=404, detail=f"Estado '{estado}' not found."
        )

    print(f"DEBUG: capital no dicionario = '{estados[estado_corrigido]['capital']}'")
    if cidade_corrigida != estados[estado_corrigido]["capital"]:  # Compare com a capital em minúsculas
        raise HTTPException(
            status_code=404, detail=f"Cidade '{cidade}' not found for Estado '{estado}'."
        )

    latitude = estados[estado_corrigido]["lat"]
    longitude = estados[estado_corrigido]["lon"]

    # ***PASSE o 'parameters'***
    weather_data = await get_weather_data(latitude, longitude, time, parameters='t_2m:C') 
    return JSONResponse(content=weather_data)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)