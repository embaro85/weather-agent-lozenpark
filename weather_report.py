import requests
import smtplib
from email.message import EmailMessage
import os

API_KEY = os.environ['OPENWEATHER_API_KEY']
EMAIL_ADDRESS = os.environ['EMAIL_USER']
EMAIL_PASSWORD = os.environ['EMAIL_PASS']

LAT = 42.6289
LON = 23.4087

url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=bg"
response = requests.get(url)
data = response.json()

weather = data['weather'][0]['description']
temp = data['main']['temp']
feels_like = data['main']['feels_like']
wind = data['wind']['speed']

msg = EmailMessage()
msg['Subject'] = 'Прогноза за времето в Лозен Парк ☀️'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

msg.set_content(f"""
Здравей, Емо! Ето прогнозата за днес:

Състояние: {weather}
Температура: {temp}°C
Усеща се като: {feels_like}°C
Вятър: {wind} м/с

Приятен ден! 🌤️
""")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
