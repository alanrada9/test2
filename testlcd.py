from rpi_lcd import LCD
import Adafruit_DHT
import time

# Initialize DHT sensor (DHT22)
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

lcd = LCD()

def read_dht_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

def read_light_status():
    # Placeholder function to simulate reading LDR
    # Replace this with your actual LDR reading code
    return "Light Detected" if True else "No Light"

try:
    while True:
        humidity, temperature = read_dht_sensor()
        light_status = read_light_status()

        # Display results on the console
        print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
        print(f"Light Status: {light_status}")

        # Display results on the LCD
        lcd.text("Temp: {:.1f}C".format(temperature), 1)
        lcd.text("Humidity: {:.1f}%".format(humidity), 2)
        lcd.text(light_status, 3)
        
        time.sleep(2)  # Wait for 2 seconds before updating readings

except KeyboardInterrupt:
    print("Exiting...")

finally:
    lcd.clear()
    lcd.text("Goodbye!", 1)
    time.sleep(2)
    lcd.clear()
