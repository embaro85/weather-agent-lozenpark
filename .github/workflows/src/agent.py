import os
from weather_fetcher import get_weather
from email_sender import send_email

def main():
    api_key = os.getenv('OPENWEATHER_API_KEY')
    email_user = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASSWORD')

    if not all([api_key, email_user, email_password]):
        print("Error: Missing environment variables!")
        return

    location = "Lozen Park, Sofia"
    weather_data = get_weather(location, api_key)

    subject = f"Weather Forecast for {location}"
    body = f"Today's weather forecast:\n{weather_data}"

    send_email(email_user, email_password, email_user, subject, body)

if __name__ == "__main__":
    main()
