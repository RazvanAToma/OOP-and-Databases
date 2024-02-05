import random

class WeatherSimulator:
    def __init__(self):
        self.sensor_data = {
            "Temperature": [],
            "Humidity": [],
            "Pressure": []
        }
        self.historical_data = {
            "Temperature": [random.uniform(-10, 40) for _ in range(365)],
            "Humidity": [random.uniform(0, 100) for _ in range(365)],
            "Pressure": [random.uniform(90000, 110000) for _ in range(365)]
        }

    def simulate_sensor(self, sensor_type, min_value, max_value):
        sensor_value = random.uniform(min_value, max_value)
        self.sensor_data[sensor_type].append(sensor_value)
        return sensor_value

    def simulate_temperature_sensor(self):
        return self.simulate_sensor("Temperature", -10, 40)

    def simulate_humidity_sensor(self):
        return self.simulate_sensor("Humidity", 0, 100)

    def simulate_pressure_sensor(self):
        return self.simulate_sensor("Pressure", 90000, 110000)

    def calculate_average(self, sensor_type):
        historical_values = self.historical_data.get(sensor_type, [])
        if historical_values:
            return sum(historical_values) / len(historical_values)
        return None

    def generate_weather_forecast(self):
        avg_temp = self.calculate_average("Temperature")
        avg_humidity = self.calculate_average("Humidity")
        avg_pressure = self.calculate_average("Pressure")

        if avg_temp is not None and avg_humidity is not None and avg_pressure is not None:
            forecast = "Weather Forecast:\n"
            if avg_temp > 25 and avg_humidity < 60 and avg_pressure > 100000:
                forecast += "It will be a hot and dry day with high pressure."
            elif avg_temp < 10 and avg_humidity > 80 and avg_pressure < 98000:
                forecast += "Expect cool and rainy conditions with low pressure."
            else:
                forecast += "The weather conditions are normal."
            print(forecast)

# Create an instance of the WeatherSimulator class
weather_simulator = WeatherSimulator()

# Simulate sensor data for 365 days
for _ in range(365):
    weather_simulator.simulate_temperature_sensor()
    weather_simulator.simulate_humidity_sensor()
    weather_simulator.simulate_pressure_sensor()

# Generate and print the weather forecast
weather_simulator.generate_weather_forecast()
