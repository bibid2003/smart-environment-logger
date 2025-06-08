 Smart Environment Logger & Dashboard

A real-time sensor simulation and monitoring system that logs environmental data, detects anomalies, and visualizes everything on an interactive web dashboard.

<div align="center">
  <img src="https://img.shields.io/badge/Flask-2.3-green?style=flat&logo=flask">
  <img src="https://img.shields.io/badge/Plotly-graph-blue?style=flat&logo=plotly">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python">
</div>







 Features

Simulates real-time environmental data (Temperature, Humidity, Motion)  
Logs data to a structured CSV file  
Sends **email alerts** for anomalies:
  -  High temperature
  -  Low humidity
  -  Motion detected  
Interactive dashboard using **Plotly**  
Date/time range filtering  
Download logged CSV data  
Easy to extend with more sensors or alerts



 Project Structure
smart-environment-logger/
│
├── main.py # Sensor simulation + logging + alerting
├── dashboard.py # Flask dashboard with data filtering & download
├── data/
│ └── sensor_log.csv # Sensor data log file
├── utils/
│ ├── sensor_simulator.py # Generates fake sensor data
│ ├── logger.py # Logs sensor data to CSV
│ └── alert_manager.py # Sends email alerts
└── README.md
 
---

 Technologies Used

- Python 3.10+
- [Flask](https://flask.palletsprojects.com/) – web server
- [Plotly](https://plotly.com/python/) – interactive graphs
- [Pandas](https://pandas.pydata.org/) – data handling
- [SMTP](https://docs.python.org/3/library/smtplib.html) – email alerting
- [Bootstrap 5](https://getbootstrap.com/) – UI styling

---

 How to Run

 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/smart-environment-logger.git
cd smart-environment-logger
```
2. Install dependencies
pip install flask pandas plotly

3. Configure Email Alerts
Open utils/alert_manager.py 
SENDER_EMAIL = "bibidbiju0@gmail.com"
APP_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "recipient_email@gmail.com"

4. Start Logging Sensor Data
python main.py
This will:

Simulate sensor data every 5 seconds
Log to data/sensor_log.csv
Send alerts if anomalies are found
 
5. Launch Dashboard
python dashboard.py
Then open http://localhost:5120/ in your browser to view:

Live sensor graph
Date/time filter
CSV download button


Author

Bibid Biju
bibidbiju0@gmail.com



