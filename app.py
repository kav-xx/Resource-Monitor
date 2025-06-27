from flask import Flask, render_template, request, jsonify
from resource_monitor import start_monitoring, stop_monitoring, get_current_metrics

app = Flask(__name__)

monitoring_status = {"active": False}

@app.route('/')
def index():
    """
    Render the main page with the frontend.
    """
    return render_template("index.html")

@app.route('/start', methods=['POST'])
def start():
    """
    Start resource monitoring if not already active.
    """
    if not monitoring_status["active"]:
        start_monitoring()
        monitoring_status["active"] = True
        return jsonify({"status": "Monitoring started"}), 200
    return jsonify({"status": "Monitoring already active"}), 400

@app.route('/stop', methods=['POST'])
def stop():
    """
    Stop resource monitoring if it's active.
    """
    if monitoring_status["active"]:
        stop_monitoring()
        monitoring_status["active"] = False
        return jsonify({"status": "Monitoring stopped"}), 200
    return jsonify({"status": "Monitoring already inactive"}), 400

@app.route('/metrics', methods=['GET'])
def metrics():
    """
    Return the current system metrics.
    """
    return get_current_metrics()

if __name__ == "__main__":
    app.run(debug=True)
