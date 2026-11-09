import requests
import sys

print("Саша, IT-32")

CITY = "Луцьк"
LAT = 50.75
LON = 25.34

URL = "https://api.open-meteo.com/v1/forecast"

try:
    params = {
        "latitude": LAT,
        "longitude": LON,
        "current": "temperature_2m,wind_speed_10m"
    }
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    
    current = data["current"]
    temp = current["temperature_2m"]
    wind = current["wind_speed_10m"]
    units = data["current_units"]
    
    print(f"{CITY} ({LAT}, {LON}): {temp} {units['temperature_2m']}, wind {wind} {units['wind_speed_10m']}")

except requests.RequestException as e:
    print(f"Помилка мережі: {e}", file=sys.stderr)
    sys.exit(1)