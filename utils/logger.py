import csv
import os

def log_to_csv(file_path, data):
    """
    Append sensor data to a CSV file.
    If the file does not exist, it creates it and adds headers.
    """
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "temperature", "humidity", "motion"])

        if not file_exists:
            writer.writeheader()  # write header if file is new

        writer.writerow(data)
