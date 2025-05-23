import requests

def get_weather(location, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',
        'lang': 'bg'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        weather_report = (
            f"{description}\n"
            f"Температура: {temperature}°C\n"
            f"Усеща се като: {feels_like}°C\n"
            f"Влажност: {humidity}%"
        )

        return weather_report

    except Exception as e:
        return f"Неуспешно получаване на данни за времето: {e}"
