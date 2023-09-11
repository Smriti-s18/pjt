import requests
import json

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = '3987515811ef2f98660d11dc80546b60'
# Replace 'CITY_NAME' with the name of the city you want to get weather data for
city_name = 'Chennai'
country_code = 'IN'

# Make the API request
base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}'
response = requests.get(base_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    weather_data = json.loads(response.text)
    
    # Extract the weather information you need
    temperature = weather_data['main']['temp']
    weather_description = weather_data['weather'][0]['description']
    
    print(f'Temperature: {temperature}°C')
    print(f'Weather Description: {weather_description}')
else:
    print('Failed to retrieve weather data. Check your API key, city name, and country code.')
