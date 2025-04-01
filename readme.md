# Documentação da API Weather

Esta documentação descreve a API Weather, que fornece dados meteorológicos em tempo real e previsões para diversas localidades.

## 1. Endpoints

* **Obter clima atual**: `/weather/current?city={cidade}&units={unidades}`
    * Retorna as condições climáticas atuais para uma determinada cidade.
    * Parâmetros:
        * `city`: (obrigatório) Nome da cidade desejada.
        * `units`: (opcional) Unidades de medida ("metric" para Celsius e metros por segundo, "imperial" para Fahrenheit e milhas por hora, padrão é "metric").
    * Exemplo de requisição: `/weather/current?city=São Paulo&units=metric`
* **Obter previsão do tempo**: `/weather/forecast?city={cidade}&units={unidades}&days={dias}`
    * Retorna a previsão do tempo para os próximos dias em uma determinada cidade.
    * Parâmetros:
        * `city`: (obrigatório) Nome da cidade desejada.
        * `units`: (opcional) Unidades de medida ("metric" ou "imperial").
        * `days`: (opcional) Número de dias para a previsão (máximo de 7 dias).
    * Exemplo de requisição: `/weather/forecast?city=Rio de Janeiro&units=metric&days=5`

## 2. Respostas

As respostas da API são formatadas em JSON.

* **Resposta para `/weather/current`**:

    ```json
    {
      "location": {
        "name": "São Paulo",
        "region": "São Paulo",
        "country": "Brazil",
        "lat": -23.55,
        "lon": -46.63,
        "tz_id": "America/Sao_Paulo",
        "localtime_epoch": 1678886400,
        "localtime": "2023-03-15 10:00"
      },
      "current": {
        "last_updated_epoch": 1678885800,
        "last_updated": "2023-03-15 09:50",
        "temp_c": 25.0,
        "temp_f": 77.0,
        "is_day": 1,
        "condition": {
          "text": "Ensolarado",
          "icon": "//[cdn.weatherapi.com/weather/64x64/day/113.png](https://www.google.com/search?q=https://cdn.weatherapi.com/weather/64x64/day/113.png)",
          "code": 1000
        },
        "wind_mph": 6.9,
        "wind_kph": 11.2,
        "wind_degree": 300,
        "wind_dir": "WNW",
        "pressure_mb": 1011.0,
        "pressure_in": 29.85,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 60,
        "cloud": 0,
        "feelslike_c": 26.1,
        "feelslike_f": 79.0,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 6.0,
        "gust_mph": 12.5,
        "gust_kph": 20.2
      }
    }
    ```

* **Resposta para `/weather/forecast`**:

    ```json
    {
      "location": {
        "name": "Rio de Janeiro",
        "region": "Rio de Janeiro",
        "country": "Brazil",
        "lat": -22.9,
        "lon": -43.21,
        "tz_id": "America/Sao_Paulo",
        "localtime_epoch": 1678886400,
        "localtime": "2023-03-15 10:00"
      },
      "forecast": {
        "forecastday": [
          {
            "date": "2023-03-15",
            "date_epoch": 1678828800,
            "day": {
              "maxtemp_c": 30.0,
              "maxtemp_f": 86.0,
              "mintemp_c": 22.0,
              "mintemp_f": 71.6,
              "avgtemp_c": 26.0,
              "avgtemp_f": 78.8,
              "maxwind_mph": 15.0,
              "maxwind_kph": 24.1,
              "totalprecip_mm": 5.0,
              "totalprecip_in": 0.20,
              "avgvis_km": 10.0,
              "avgvis_miles": 6.0,
              "avghumidity": 70.0,
              "daily_will_it_rain": 1,
              "daily_chance_of_rain": 80,
              "daily_will_it_snow": 0,
              "daily_chance_of_snow": 0,
              "condition": {
                "text": "Chuva",
                "icon": "//[cdn.weatherapi.com/weather/64x64/day/302.png](https://www.google.com/search?q=https://cdn.weatherapi.com/weather/64x64/day/302.png)",
                "code": 1189
              },
              "uv": 7.0
            },
            "astro": {
              "sunrise": "06:00 AM",
              "sunset": "06:00 PM",
              "moonrise": "04:00 PM",
              "moonset": "02:00 AM",
              "moon_phase": "Waxing Gibbous",
              "moon_illumination": 75
            }
          },
          {...}
        ]
      }
    }
    ```

## 3. Códigos de Erro

* **400 Bad Request**: Requisição inválida (parâmetros ausentes ou incorretos).
* **404 Not Found**: Cidade não encontrada.
* **500 Internal Server Error**: Erro interno do servidor.

## 4. Exemplos de Uso

* **Usando `curl`**:

    ```bash
    curl "[http://sua-api.com/weather/current?city=Londres&units=metric](http://sua-api.com/weather/current?city=Londres&units=metric)"
    curl "[http://sua-api.com/weather/forecast?city=Buenos](http://sua-api.com/weather/forecast?city=Buenos) Aires&units=imperial&days=3"
    ```

* **Usando Python**:

    ```python
    import requests

    response = requests.get("[http://sua-api.com/weather/current?city=Tokyo](http://sua-api.com/weather/current?city=Tokyo)")
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Erro: {response.status_code}")

    response = requests.get("[http://sua-api.com/weather/forecast?city=Paris&days=2](http://sua-api.com/weather/forecast?city=Paris&days=2)")
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Erro: {response.status_code}")
    ```

## 5. Notas

* A API Weather utiliza dados de diversas fontes para fornecer informações precisas e atualizadas.
* A precisão das previsões pode variar dependendo da localização e do tempo.
* É recomendado consultar a documentação da API Weather periodicamente, pois podem haver atualizações e melhorias.