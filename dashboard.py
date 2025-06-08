from flask import Flask, render_template_string, request, send_file
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import os
from datetime import datetime

app = Flask(__name__)
CSV_FILE_PATH = "data/sensor_log.csv"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Smart Environment Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body style="background-color: #f8f9fa;">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">🌿 Smart Environment Dashboard</a>
        </div>
    </nav>

    <div class="container mt-5">
        <form method="get" class="row g-3 mb-4">
            <div class="col-md-5">
                <label for="start" class="form-label">Start Time</label>
                <input type="datetime-local" id="start" name="start" class="form-control" value="{{ start }}">
            </div>
            <div class="col-md-5">
                <label for="end" class="form-label">End Time</label>
                <input type="datetime-local" id="end" name="end" class="form-control" value="{{ end }}">
            </div>
            <div class="col-md-2 d-flex align-items-end">
                <button type="submit" class="btn btn-primary w-100">Filter</button>
            </div>
        </form>

        <div class="card shadow-lg">
            <div class="card-body">
                <h5 class="card-title text-center mb-4">📈 Sensor Data Visualization</h5>
                {{ graph_html|safe }}
                <div class="text-center mt-4">
                    <a href="/download" class="btn btn-primary">⬇️ Download CSV</a>
                </div>
            </div>
        </div>
    </div>

    <footer class="text-center mt-5 text-muted">
        <p>&copy; 2025 | Smart Logger by Bibid B</p>
    </footer>
</body>
</html>
"""

@app.route("/")
def dashboard():
    if not os.path.exists(CSV_FILE_PATH):
        return "No sensor data available. Please run main.py first."

    df = pd.read_csv(CSV_FILE_PATH)

    if df.empty or "timestamp" not in df.columns:
        return "CSV file is empty or corrupt. Please generate valid data."

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Get start and end from query params
    start = request.args.get("start")
    end = request.args.get("end")

    # Filter data if both start and end are provided
    if start and end:
        try:
            start_dt = datetime.strptime(start, "%Y-%m-%dT%H:%M")
            end_dt = datetime.strptime(end, "%Y-%m-%dT%H:%M")
            df = df[(df["timestamp"] >= start_dt) & (df["timestamp"] <= end_dt)]
        except ValueError:
            pass  # Invalid input is silently ignored

    # Plot
    trace_temp = go.Scatter(x=df["timestamp"], y=df["temperature"], name="Temperature (°C)", line=dict(color="red"))
    trace_hum = go.Scatter(x=df["timestamp"], y=df["humidity"], name="Humidity (%)", line=dict(color="blue"))

    layout = go.Layout(title="Filtered Sensor Data", xaxis=dict(title="Timestamp"), yaxis=dict(title="Value"))
    fig = go.Figure(data=[trace_temp, trace_hum], layout=layout)

    graph_html = pyo.plot(fig, output_type="div", include_plotlyjs=True)

    return render_template_string(HTML_TEMPLATE, graph_html=graph_html, start=start or "", end=end or "")

@app.route("/download")
def download_csv():
    if os.path.exists(CSV_FILE_PATH):
        return send_file(CSV_FILE_PATH, as_attachment=True)
    return "CSV file not found.", 404

if __name__ == "__main__":
    app.run(debug=True, port=5120)


