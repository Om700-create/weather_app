from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
import requests
import sys

# Define the WeatherApp class
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("🌤 Real-Time Weather App")
        self.setGeometry(100, 100, 500, 500)
        self.setStyleSheet("background-color: #1e1e2e;")

        # Initialize UI components
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()

        # Title label
        self.title_label = QLabel("🌦 Weather App", self)
        self.title_label.setFont(QFont("Arial", 22, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.title_label)

        # City input label
        self.city_label = QLabel("🏙 Enter City Name:", self)
        self.city_label.setFont(QFont("Arial", 14))
        self.city_label.setStyleSheet("color: #b0b0b0;")
        layout.addWidget(self.city_label)

        # City input field
        self.city_input = QLineEdit(self)
        self.city_input.setFont(QFont("Arial", 14))
        self.city_input.setStyleSheet("padding: 8px; border: 1px solid #5c5c5c; border-radius: 5px; background-color: #2e2e3e; color: #ffffff;")
        layout.addWidget(self.city_input)

        # Get weather button
        self.get_weather_button = QPushButton("🌍 Get Weather", self)
        self.get_weather_button.setFont(QFont("Arial", 14))
        self.get_weather_button.setStyleSheet(
            "background-color: #0078d7; color: #ffffff; border: none; padding: 10px; border-radius: 5px;"
        )
        self.get_weather_button.clicked.connect(self.fetch_weather)
        layout.addWidget(self.get_weather_button)

        # Weather information labels
        self.weather_info_label = QLabel("", self)
        self.weather_info_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.weather_info_label.setAlignment(Qt.AlignCenter)
        self.weather_info_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.weather_info_label)

        self.temperature_label = QLabel("", self)
        self.temperature_label.setFont(QFont("Arial", 14))
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setStyleSheet("color: #00ff99;")
        layout.addWidget(self.temperature_label)

        self.description_label = QLabel("", self)
        self.description_label.setFont(QFont("Arial", 14))
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setStyleSheet("color: #bbbbbb;")
        layout.addWidget(self.description_label)

        self.humidity_label = QLabel("", self)
        self.humidity_label.setFont(QFont("Arial", 14))
        self.humidity_label.setAlignment(Qt.AlignCenter)
        self.humidity_label.setStyleSheet("color: #bbbbbb;")
        layout.addWidget(self.humidity_label)

        self.wind_speed_label = QLabel("", self)
        self.wind_speed_label.setFont(QFont("Arial", 14))
        self.wind_speed_label.setAlignment(Qt.AlignCenter)
        self.wind_speed_label.setStyleSheet("color: #bbbbbb;")
        layout.addWidget(self.wind_speed_label)

        # Set layout to the main window
        self.setLayout(layout)

    def fetch_weather(self):
        # API key and endpoint
        api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        # Get the city name from the input field
        city_name = self.city_input.text().strip()

        if not city_name:
            self.weather_info_label.setText("⚠️ Please enter a city name.")
            self.temperature_label.setText("")
            self.description_label.setText("")
            self.humidity_label.setText("")
            self.wind_speed_label.setText("")
            return

        # Make API request
        params = {"q": city_name, "appid": api_key, "units": "metric"}
        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if data["cod"] == 200:
                # Extract weather data
                city = data["name"]
                country = data["sys"]["country"]
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"].capitalize()
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]

                # Update labels with weather information
                self.weather_info_label.setText(f"🌍 Weather in {city}, {country}:")
                self.temperature_label.setText(f"🌡️ Temperature: {temperature} °C")
                self.description_label.setText(f"🌤️ Description: {description}")
                self.humidity_label.setText(f"💧 Humidity: {humidity}%")
                self.wind_speed_label.setText(f"🌬️ Wind Speed: {wind_speed} m/s")
            else:
                self.weather_info_label.setText("❌ City not found. Please try again.")
                self.temperature_label.setText("")
                self.description_label.setText("")
                self.humidity_label.setText("")
                self.wind_speed_label.setText("")
        except Exception as e:
            self.weather_info_label.setText("❗ Error fetching weather data.")
            self.temperature_label.setText("")
            self.description_label.setText("")
            self.humidity_label.setText("")
            self.wind_speed_label.setText("")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
