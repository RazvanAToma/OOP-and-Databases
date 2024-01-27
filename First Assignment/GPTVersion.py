import random

class WeatherSensor:
    def __init__(self, sensor_type, historical_data):
        self.sensor_type = sensor_type
        self.sensor_data = []
        self.historical_data = historical_data

    def simulate_sensor_reading(self):
        reading = random.uniform(*self.historical_data["range"])
        self.sensor_data.append(reading)
        return reading

    def calculate_average(self):
        historical_values = self.historical_data["data"]
        if historical_values:
            return sum(historical_values) / len(historical_values)
        return None

class WeatherSimulator:
    def __init__(self):
        self.sensors = {
            "Temperature": WeatherSensor("Temperature", {"range": (-10, 40), "data": []}),
            "Humidity": WeatherSensor("Humidity", {"range": (0, 100), "data": []}),
            "Pressure": WeatherSensor("Pressure", {"range": (90000, 110000), "data": []}),
        }

    def simulate_weather_data(self, days=365):
        for _ in range(days):
            for sensor_type, sensor in self.sensors.items():
                sensor.simulate_sensor_reading()

    def generate_weather_forecast(self):
        avg_temp = self.sensors["Temperature"].calculate_average()
        avg_humidity = self.sensors["Humidity"].calculate_average()
        avg_pressure = self.sensors["Pressure"].calculate_average()

        if avg_temp is not None and avg_humidity is not None and avg_pressure is not None:
            forecast = "Weather Forecast:\n"
            if avg_temp > 25 and avg_humidity < 60 and avg_pressure > 100000:
                forecast += "It will be a hot and dry day with high pressure."
            elif avg_temp < 10 and avg_humidity > 80 and avg_pressure < 98000:
                forecast += "Expect cool and rainy conditions with low pressure."
            else:
                forecast += "The weather conditions are normal."
            print(forecast)

# Instantiate the WeatherSimulator
simulator = WeatherSimulator()

# Simulate sensor data for 365 days
simulator.simulate_weather_data()

# Generate and print the weather forecast
simulator.generate_weather_forecast()
