import requests


def obtener_tiempo(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    print("URL:", url)
    response = requests.get(url)

    print("Respuesta:", response.json())

    if response.status_code == 200:
        clima = response.json()["weather"][0]["description"]
        temperatura = response.json()["main"]["temp"]
        sensacion_termica = response.json()["main"]["feels_like"]
        print(f"El clima en {ciudad} es: {clima}°C")
        print(f"Temperatura: {temperatura}")
        print(f"Sensación térmica: {sensacion_termica}°C")
    else:
        print("Error al obtener el tiempo. Verifica la ciudad y la API key.")


ciudad = "Guasave"
api_key = "7b8dcdc023d38c6e99aa6a15d01ac41e"

obtener_tiempo(ciudad, api_key)

