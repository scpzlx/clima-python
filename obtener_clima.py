import requests


def obtener_tiempo(nombre_ciudad, clave_api):
    url = (
        "http://api.openweathermap.org/data/2.5/weather"
        f"?q={nombre_ciudad}&appid={clave_api}&units=metric"
    )
    print("URL:", url)
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()
        clima = datos["weather"][0]["description"]
        temperatura = datos["main"]["temp"]
        sensacion_termica = datos["main"]["feels_like"]

        print(f"El clima en {nombre_ciudad} es: {clima}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Sensación térmica: {sensacion_termica}°C")
    else:
        print("Error al obtener el tiempo. Verifica la ciudad y la API key.")


CIUDAD = "Guasave"
API_KEY = "7b8dcdc023d38c6e99aa6a15d01ac41e"
obtener_tiempo(CIUDAD, API_KEY)
