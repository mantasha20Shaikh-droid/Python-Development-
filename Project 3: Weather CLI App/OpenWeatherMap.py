#pip install requests
import requests


def get_weather(city):
    api_key = "YOUR_API_KEY"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Weather:", weather)

    else:
        print("City not found")


def main():
    city = input("Enter city name: ")
    get_weather(city)


if __name__ == "__main__":
    main()
#python weather.py
#Enter city name: Surat

#City: Surat
#Temperature: 29.5 °C
#Weather: scattered clouds
