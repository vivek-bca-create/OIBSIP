import sys
import requests


def fetch_weather_data(city_name, api_key):
    """Fetches real-time weather data from OpenWeatherMap API using dynamic keys."""
    base_url = "https://openweathermap.org"
    parameters = {"q": city_name, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=parameters, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("Error: City not found. Please verify the name.")
            return None
        elif response.status_code == 401:
            print("Error: Invalid or inactive API Key. Please check your credentials.")
            return None
        else:
            print(f"Error: Server responded with status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as error:
        print(f"Network Connection Error: {error}")
        return None


def display_weather(data):
    """Parses and renders JSON weather information cleanly in the terminal."""
    if not data:
        return

    city = data.get("name")
    country = data.get("sys", {}).get("country")
    main_info = data.get("main", {})
    temperature = main_info.get("temp")
    humidity = main_info.get("humidity")
    wind_speed = data.get("wind", {}).get("speed")
    weather_desc = data.get("weather", [{}]).get("description", "N/A")

    print("\n" + "=" * 40)
    print(f" Weather Report for: {city}, {country} ")
    print("=" * 40)
    print(f"Condition   : {weather_desc.capitalize()}")
    print(f"Temperature : {temperature}°C")
    print(f"Humidity    : {humidity}%")
    print(f"Wind Speed  : {wind_speed} m/s")
    print("=" * 40 + "\n")


def main():
    """Main application loop with safe dynamic credential input framework."""
    print("--- Welcome to the Secure Basic Weather Application ---")

    # Asking for dynamic key input to keep repository secure from leaks
    api_key = input("Please enter your OpenWeatherMap API Key: ").strip()

    if not api_key:
        print("Configuration Error: API Key cannot be empty.")
        sys.exit(1)

    while True:
        city_name = input("Enter city name (or type 'exit' to quit): ").strip()

        if city_name.lower() == "exit":
            print("Thank you for using the Weather App. Goodbye!")
            break

        if not city_name:
            print("Input cannot be empty. Please enter a valid location.")
            continue

        weather_json = fetch_weather_data(city_name, api_key)
        if weather_json:
            display_weather(weather_json)


if __name__ == "__main__":
    main()
