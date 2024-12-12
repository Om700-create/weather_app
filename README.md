# 🌤 Real-Time Weather App

This is a simple desktop application that provides real-time weather information using PyQt5 and OpenWeatherMap API. It allows users to enter the name of a city and get details like temperature, weather description, humidity, and wind speed.

## Features
- **Enter City Name**: Users can input the name of a city to fetch its weather.
- **Real-Time Weather**: Get up-to-date weather data including temperature, description, humidity, and wind speed.
- **User-Friendly Interface**: Clean and easy-to-use interface built with PyQt5.

## Requirements
- Python 3.x
- PyQt5
- `requests` library for making API requests.

## Installation

1. Clone the repository or download the source code.

    ```bash
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. Install the required dependencies using `pip`.

    ```bash
    pip install pyqt5 requests
    ```

3. Sign up for an API key from OpenWeatherMap:
    - Go to [OpenWeatherMap API](https://openweathermap.org/api) and create an account to get an API key.

4. Replace the placeholder API key in the code with your actual key:
    ```python
    api_key = "your_api_key_here"
    ```

## How to Run

1. After setting up the environment and replacing the API key, run the app with:

    ```bash
    python weather_app.py
    ```

2. The app window will open, where you can enter a city name and click the "Get Weather" button to fetch the weather details.

## Example

1. Open the app and type the name of a city, e.g., "London".
2. Click the **🌍 Get Weather** button.
3. The app will display:
    - 🌡️ Temperature
    - 🌤️ Weather Description
    - 💧 Humidity
    - 🌬️ Wind Speed

## Screenshots
![Weather App Screenshot](https://github.com/Om700-create/weather_app/blob/298a11e8c6cd675c84e635b836f753d0a77216a9/Screenshot%202024-12-12%20152402.png)

## Troubleshooting
- If you get an error like "❗ Error fetching weather data," ensure your API key is correct and your internet connection is stable.
- Make sure the city name is entered correctly.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenWeatherMap for the weather data API.
- PyQt5 for the GUI framework.

---

Feel free to customize and contribute to the project. Enjoy using the weather app! 🌦


