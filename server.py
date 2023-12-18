import paho.mqtt.client as mqtt
import psycopg2
import time
import random

# MQTT Setup
broker_address = "localhost"
client = mqtt.Client("WeatherStation")
client.connect(broker_address)

# PostgreSQL Database Connection Setup
conn = psycopg2.connect(
    host="localhost",
    database="weatherdata",
    user="postgres",  # Replace with your PostgreSQL username
    password="soot"  # Replace with your PostgreSQL password
)
cursor = conn.cursor()

while True:
    temperature = random.uniform(15, 30)
    humidity = random.uniform(30, 90)
    payload = f"{temperature},{humidity}"

    # Publish to MQTT
    client.publish("weather/data", payload)

    # Insert into PostgreSQL Database
    cursor.execute("INSERT INTO weatherlogs (temperature, humidity, timestamp) VALUES (%s, %s, CURRENT_TIMESTAMP)", (temperature, humidity))
    conn.commit()

    time.sleep(5)

# Close PostgreSQL connection
cursor.close()
conn.close()
