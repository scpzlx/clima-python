import requests


def obtener_tiempo(ciudad, api_key):
    url = (
        "http://api.openweathermap.org/data/2.5/weather"
        f"?q={ciudad}&appid={api_key}&units=metric"
    )
    print("URL:", url)
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()
        clima = datos["weather"][0]["description"]
        temperatura = datos["main"]["temp"]
        sensacion_termica = datos["main"]["feels_like"]

        print(f"El clima en {ciudad} es: {clima}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Sensación térmica: {sensacion_termica}°C")
    else:
        print("Error al obtener el tiempo. Verifica la ciudad y la API key.")


ciudad = "Guasave"
api_key = "7b8dcdc023d38c6e99aa6a15d01ac41e"
obtener_tiempo(ciudad, api_key)
