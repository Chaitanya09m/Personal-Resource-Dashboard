from flask import Flask, jsonify, request, render_template
from modules import network_diagnostics
from modules import system_monitor  # Import the system monitor module

import os

# Flask App Initialization
app = Flask(
    __name__,
    template_folder="templates",  # Path to the templates directory
    static_folder="static"        # Path to the static directory
)

# Debugging: Verify template folder path
print("Template Folder Path:", os.path.abspath(app.template_folder))
print("Templates Directory Content:", os.listdir(app.template_folder))

# Dashboard Route
@app.route("/")
def dashboard():
    print("Rendering dashboard.html")  # Debugging
    return render_template("dashboard.html")

# Ping Host Endpoint
@app.route("/ping_host", methods=["POST"])
def ping_host():
    host = request.form.get("host")  # Fixed for form data
    if not host:
        return jsonify({"error": "Host is required"}), 400

    result = network_diagnostics.ping_host(host)
    return render_template("result.html", result=result)

# Traceroute Endpoint
@app.route("/traceroute", methods=["POST"])
def traceroute():
    host = request.form.get("host")  # Fixed for form data
    if not host:
        return jsonify({"error": "Host is required"}), 400

    result = network_diagnostics.traceroute(host)
    return render_template("result.html", result=result)

# System Stats Endpoint
@app.route("/system_stats")
def system_stats():
    # Fetch system stats using system_monitor module
    stats = {
        "cpu": system_monitor.cpu_usage(),
        "memory": system_monitor.memory_usage(),
        "disk": system_monitor.disk_usage(),
        "uptime": system_monitor.system_uptime(),
    }
    print("System Stats:", stats)  # Debugging
    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True)
