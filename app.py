from flask import Flask, jsonify, request
from modules import network_diagnostics
from modules import system_monitor  # Import the system monitor module

app = Flask(__name__)  # Initialize the Flask app

@app.route("/ping_host", methods=["POST"])
def ping_host():
    host = request.json.get("host")
    if not host:
        return jsonify({"error": "Host is required"}), 400
    
    result = network_diagnostics.ping_host(host)
    return jsonify({"result": result})

@app.route("/traceroute", methods=["POST"])
def traceroute():
    host = request.json.get("host")
    if not host:
        return jsonify({"error": "Host is required"}), 400
    
    result = network_diagnostics.traceroute(host)
    return jsonify({"result": result})

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
