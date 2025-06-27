import psutil
import json
import time
from collections import deque
import matplotlib.pyplot as plt
import threading

# History deque for plotting
history_length = 60
cpu_history = deque(maxlen=history_length)
memory_history = deque(maxlen=history_length)
disk_history = deque(maxlen=history_length)
rx_history = deque(maxlen=history_length)
tx_history = deque(maxlen=history_length)

# Monitoring control variables
monitoring = False
last_rx, last_tx = 0, 0

def get_metrics():
    """Get system metrics."""
    global last_rx, last_tx
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    rx_bytes, tx_bytes = psutil.net_io_counters().bytes_recv, psutil.net_io_counters().bytes_sent

    # Calculate network deltas
    rx_rate = rx_bytes - last_rx
    tx_rate = tx_bytes - last_tx
    last_rx, last_tx = rx_bytes, tx_bytes

    # Save to history
    cpu_history.append(cpu)
    memory_history.append(memory)
    disk_history.append(disk)
    rx_history.append(rx_rate)
    tx_history.append(tx_rate)

    return {
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk,
        "network_in": rx_rate,
        "network_out": tx_rate,
    }

def write_to_json(data):
    """Write system metrics to a JSON file."""
    try:
        with open("data.json", "w") as fp:
            json.dump(data, fp, indent=2)
    except Exception as e:
        print(f"Error writing to JSON: {e}")

def plot_graphs():
    """Plot real-time graphs for system metrics."""
    plt.clf()
    time_range = range(-len(cpu_history), 0)

    try:
        # CPU Usage
        plt.subplot(2, 2, 1)
        plt.plot(time_range, list(cpu_history), label="CPU Usage (%)", color="blue")
        plt.title("CPU Usage")
        plt.ylim(0, 100)
        plt.xlabel("Time (s)")
        plt.ylabel("Percentage")
        plt.grid(True)

        # Memory Usage
        plt.subplot(2, 2, 2)
        plt.plot(time_range, list(memory_history), label="Memory Usage (%)", color="green")
        plt.title("Memory Usage")
        plt.ylim(0, 100)
        plt.xlabel("Time (s)")
        plt.ylabel("Percentage")
        plt.grid(True)

        # Disk Usage
        plt.subplot(2, 2, 3)
        plt.plot(time_range, list(disk_history), label="Disk Usage (%)", color="red")
        plt.title("Disk Usage")
        plt.ylim(0, 100)
        plt.xlabel("Time (s)")
        plt.ylabel("Percentage")
        plt.grid(True)

        # Network Stats
        plt.subplot(2, 2, 4)
        plt.plot(time_range, list(rx_history), label="RX Bytes", color="purple")
        plt.plot(time_range, list(tx_history), label="TX Bytes", color="orange")
        plt.title("Network Traffic (Bytes)")
        plt.xlabel("Time (s)")
        plt.ylabel("Bytes")
        plt.grid(True)
        plt.legend()

        plt.tight_layout()
        plt.pause(0.1)
    except Exception as e:
        print(f"Error updating plots: {e}")

def monitor_system():
    """Continuously monitor system metrics."""
    global monitoring
    plt.ion()
    while monitoring:
        try:
            metrics = get_metrics()
            write_to_json(metrics)
            plot_graphs()
            time.sleep(1)
        except Exception as e:
            print(f"Monitoring error: {e}")
            time.sleep(1)

def start_monitoring():
    """Start monitoring in a separate thread."""
    global monitoring
    if not monitoring:
        monitoring = True
        thread = threading.Thread(target=monitor_system, daemon=True)
        thread.start()

def stop_monitoring():
    """Stop monitoring."""
    global monitoring
    monitoring = False

def get_current_metrics():
    """Get the most recent system metrics."""
    return get_metrics()
