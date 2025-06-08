import time
from utils.sensor_simulator import simulate_sensors
from utils.logger import log_to_csv
from utils.alert_manager import send_email_alert

# Path to the CSV file
CSV_FILE_PATH = "data/sensor_log.csv"

print("📡 Smart Environment Logger Started")
print("-----------------------------------\n")

try:
    while True:
        # Simulate sensors
        sensor_data = simulate_sensors()

        # Log data to CSV
        log_to_csv(CSV_FILE_PATH, sensor_data)

        # Print data to terminal
        print(f"[{sensor_data['timestamp']}] Temp: {sensor_data['temperature']}°C | "
              f"Humidity: {sensor_data['humidity']}% | Motion: {sensor_data['motion']}")

        # --- Anomaly Detection and Alerts ---
        if sensor_data["temperature"] > 40:
            send_email_alert("🔥 High Temperature Alert!",
                             f"Temperature reached {sensor_data['temperature']}°C at {sensor_data['timestamp']}")

        if sensor_data["humidity"] < 35:
            send_email_alert("💧 Low Humidity Alert!",
                             f"Humidity dropped to {sensor_data['humidity']}% at {sensor_data['timestamp']}")

        if sensor_data["motion"]:
            send_email_alert("🚨 Motion Detected!",
                             f"Motion was detected at {sensor_data['timestamp']}")

        # Wait before next reading
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Stopped by user. Logging ended.")

