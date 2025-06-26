Here’s a complete `README.md` file for your project, including file structure and key features:

---

```markdown
# 🖥️ Real-Time System Resource Monitor

A lightweight real-time system monitoring web app built using **Flask**, **psutil**, and **Matplotlib**. It tracks system performance metrics including CPU, memory, disk, and network usage, with dynamic visualizations and a JSON data log.

---

## 🔧 Features

- ✅ Monitor CPU, memory, disk, and network I/O usage in real time  
- 📈 Live-updating graphs using `matplotlib`  
- 🌐 Web interface to start and stop monitoring  
- 💾 System metrics logged into `data.json`  
- 🧩 Modular design with clean frontend separation (HTML, CSS, JS)

---

## 📁 Project Structure

```

.
├── app.py                     # Flask app entry point
├── resource\_monitor.py       # Handles system monitoring, graphing, and JSON logging
├── templates/
│   └── index.html            # Frontend HTML interface
├── static/
│   ├── css/
│   │   └── style.css         # Styles for the web UI
│   └── js/
│       └── script.js         # JavaScript for frontend interaction
├── data.json                 # Output JSON file (generated at runtime)
└── README.md                 # Project documentation

````

---

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install flask psutil matplotlib
````

### 2. Run the Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 📊 How It Works

* `resource_monitor.py`: Collects system metrics every second, writes to JSON, and updates graphs.
* `app.py`: Flask backend handles routing and control APIs (`/start`, `/stop`, `/metrics`).
* `index.html`: UI to start/stop monitoring and display live data (requires JS for interactivity).
* `style.css` and `script.js`: Handle frontend styling and interactivity.

---

## 📝 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

Developed by \[Kavyasri V J]. Contributions welcome!


