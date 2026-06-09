import requests
import json

API_KEY = "02d14d537c4c16cee23ec6bd608c9a7a"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 1)

def kelvin_to_fahrenheit(kelvin):
    return round((kelvin - 273.15) * 9/5 + 32, 1)

def get_weather_emoji(condition):
    condition = condition.lower()
    if "clear" in condition:
        return "☀️"
    elif "cloud" in condition:
        return "☁️"
    elif "rain" in condition or "drizzle" in condition:
        return "🌧️"
    elif "snow" in condition:
        return "❄️"
    elif "thunder" in condition or "storm" in condition:
        return "⛈️"
    elif "mist" in condition or "fog" in condition or "haze" in condition:
        return "🌫️"
    elif "wind" in condition:
        return "💨"
    else:
        return "🌡️"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Check for errors
        if response.status_code == 401:
            print("\n❌ Error: Invalid API key. Please check your API key.")
            return
        elif response.status_code == 404:
            print(f"\n❌ Error: City '{city}' not found. Please check the spelling.")
            return
        elif response.status_code != 200:
            print(f"\n❌ Error: {data.get('message', 'Something went wrong.')}")
            return

        # Extract data from JSON response
        city_name     = data["name"]
        country       = data["sys"]["country"]
        temp_k        = data["main"]["temp"]
        feels_like_k  = data["main"]["feels_like"]
        humidity      = data["main"]["humidity"]
        condition     = data["weather"][0]["main"]
        description   = data["weather"][0]["description"].capitalize()
        wind_speed    = data["wind"]["speed"]           # m/s
        visibility    = data.get("visibility", "N/A")   # meters

        temp_c  = kelvin_to_celsius(temp_k)
        temp_f  = kelvin_to_fahrenheit(temp_k)
        feel_c  = kelvin_to_celsius(feels_like_k)
        feel_f  = kelvin_to_fahrenheit(feels_like_k)
        emoji   = get_weather_emoji(condition)

        # Display weather report
        print("\n" + "=" * 45)
        print(f"  {emoji}  Weather Report: {city_name}, {country}")
        print("=" * 45)
        print(f"  Condition    : {description}")
        print(f"  Temperature  : {temp_c}°C  /  {temp_f}°F")
        print(f"  Feels Like   : {feel_c}°C  /  {feel_f}°F")
        print(f"  Humidity     : {humidity}%")
        print(f"  Wind Speed   : {wind_speed} m/s")
        if visibility != "N/A":
            print(f"  Visibility   : {visibility // 1000} km")
        print("=" * 45)

    except requests.exceptions.ConnectionError:
        print("\n❌ Network Error: Could not connect. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("\n❌ Timeout Error: The request took too long. Try again.")
    except KeyError as e:
        print(f"\n❌ Data Error: Missing expected field {e}.")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")

def main():
    print("╔══════════════════════════════════════════╗")
    print("║        🌤️  Weather App - Console          ║")
    print("║     Powered by OpenWeatherMap API         ║")
    print("╚══════════════════════════════════════════╝")
    print("\nType 'quit' or 'exit' to stop the program.\n")

    while True:
        city = input("🌍 Enter city name: ").strip()

        if not city:
            print("⚠️  Please enter a city name.\n")
            continue

        if city.lower() in ("quit", "exit"):
            print("\n👋 Goodbye! Stay weather-aware!")
            break

        fetch_weather(city)
        print()

if __name__ == "__main__":
    main()