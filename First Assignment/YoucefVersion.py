import random

sensor_data = { # Initialize data storage
    "Temperature": [],
    "Humidity": [],
    "Pressure": []
}
historical_data = { # Initialize historical data
    "Temperature": [random.uniform(-10, 40) for _ in range(365)],
    "Humidity": [random.uniform(0, 100) for _ in range(365)],
    "Pressure": [random.uniform(90000, 110000) for _ in range(365)]
}
def simulate_temperature_sensor(): # Simulate a temperature sensor
    temperature = random.uniform(-10, 40)
    sensor_data["Temperature"].append(temperature)
    return temperature

def simulate_humidity_sensor(): # Simulate a humidity sensor
    humidity = random.uniform(0, 100)
    sensor_data["Humidity"].append(humidity)
    return humidity

def simulate_pressure_sensor(): # Simulate a pressure sensor
    pressure = random.uniform(90000, 110000)
    sensor_data["Pressure"].append(pressure)
    return pressure

def calculate_average(sensor_type): # Calculate the average of a sensor's historical data
    historical_values = historical_data.get(sensor_type, [])
    if historical_values:
        return sum(historical_values) / len(historical_values)
    return None

def generate_weather_forecast(): # Generate a weather forecast
    avg_temp = calculate_average("Temperature")
    avg_humidity = calculate_average("Humidity")
    avg_pressure = calculate_average("Pressure")
    if avg_temp is not None and avg_humidity is not None and avg_pressure is not None:
        forecast = "Weather Forecast:\n"
        if avg_temp > 25 and avg_humidity < 60 and avg_pressure > 100000:
            forecast += "It will be a hot and dry day with high pressure."
        elif avg_temp < 10 and avg_humidity > 80 and avg_pressure < 98000:
            forecast += "Expect cool and rainy conditions with low pressure."
        else:
            forecast += "The weather conditions are normal."
        print(forecast)


for _ in range(365):
    simulate_temperature_sensor()
    simulate_humidity_sensor()
    simulate_pressure_sensor()
generate_weather_forecast()