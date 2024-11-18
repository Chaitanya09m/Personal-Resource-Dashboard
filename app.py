from flask import Flask, jsonify
from modules import system_monitor  # Import the system_monitor module

app = Flask(__name__)  # Initialize the Flask app

@app.route("/system_stats")
def system_stats():
    # Fetch system stats using system_monitor module
    stats = {
        "cpu": system_monitor.cpu_usage(),
        "memory": system_monitor.memory_usage(),
        "disk": system_monitor.disk_usage(),
        "uptime": system_monitor.system_uptime(),
    }
    return jsonify(stats)  # Return stats as JSON

if __name__ == "__main__":
    app.run(debug=True)
