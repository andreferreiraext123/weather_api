estados = {
    "Acre": {"capital": "Rio Branco", "lat": -9.97499, "lon": -67.8243},
    "Alagoas": {"capital": "Maceió", "lat": -9.66599, "lon": -35.735},
    "Amapá": {"capital": "Macapá", "lat": 0.0349, "lon": -51.0694},
    "Amazonas": {"capital": "Manaus", "lat": -3.11866, "lon": -60.0212},
    "Bahia": {"capital": "Salvador", "lat": -12.9714, "lon": -38.5014},
    "Ceará": {"capital": "Fortaleza", "lat": -3.71722, "lon": -38.5431},
    "Distrito Federal": {"capital": "Brasília", "lat": -15.7795, "lon": -47.9297},
    # Adicione os demais estados aqui...
}

# Exemplo de uso:
estado_escolhido = "Bahia"
lat, lon = estados[estado_escolhido]["lat"], estados[estado_escolhido]["lon"]

print(f"Coordenadas de {estado_escolhido}: Latitude {lat}, Longitude {lon}")
