let isMonitoring = false;

// Function to fetch and update metrics
const fetchMetrics = async () => {
  if (isMonitoring) {
    try {
      const response = await fetch('/metrics');
      const metrics = await response.json();

      // Update the UI with metrics
      cpuData.push(metrics.cpu_usage);
      memoryData.push(metrics.memory_usage);
      diskData.push(metrics.disk_usage);
      rxData.push(metrics.network_in);
      txData.push(metrics.network_out);

      // Trim datasets to history length
      cpuData = cpuData.slice(-historyLength);
      memoryData = memoryData.slice(-historyLength);
      diskData = diskData.slice(-historyLength);
      rxData = rxData.slice(-historyLength);
      txData = txData.slice(-historyLength);

      // Update charts
      updateChart(cpuChart, cpuData);
      updateChart(memoryChart, memoryData);
      updateChart(diskChart, diskData);
      updateChart(networkChart, rxData.map((val, i) => val + txData[i]));
    } catch (error) {
      console.error('Error fetching metrics:', error);
    }
  }
};

// Function to start monitoring
const startMonitoring = async () => {
  try {
    await fetch('/start', { method: 'POST' });
    isMonitoring = true;
  } catch (error) {
    console.error('Error starting monitoring:', error);
  }
};

// Function to stop monitoring
const stopMonitoring = async () => {
  try {
    await fetch('/stop', { method: 'POST' });
    isMonitoring = false;
  } catch (error) {
    console.error('Error stopping monitoring:', error);
  }
};

// Attach event listeners to buttons
document.getElementById('startButton').addEventListener('click', startMonitoring);
document.getElementById('stopButton').addEventListener('click', stopMonitoring);

// Update metrics every second
setInterval(fetchMetrics, 1000);

document.getElementById("startButton").addEventListener("click", function () {
  fetch("/start", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
  })
      .then((response) => response.json())
      .then((data) => {
          alert(data.status);
      })
      .catch((error) => {
          console.error("Error starting monitoring:", error);
      });
});

document.getElementById("stopButton").addEventListener("click", function () {
  fetch("/stop", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
  })
      .then((response) => response.json())
      .then((data) => {
          alert(data.status);
      })
      .catch((error) => {
          console.error("Error stopping monitoring:", error);
      });
});
