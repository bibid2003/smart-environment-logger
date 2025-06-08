import random
from datetime import datetime

def simulate_sensors():
    """
    Simulate temperature (°C), humidity (%), and motion (True/False)
    Returns a dictionary with the values.
    """
    temperature = round(random.uniform(20.0, 45.0), 2)   
    humidity = round(random.uniform(30.0, 80.0), 2)       
    motion = random.choice([True, False])                 

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": temperature,
        "humidity": humidity,
        "motion": motion
    }
