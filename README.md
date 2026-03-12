# 🛡️ Sentinel-Automation: Web-Health-Monitor

A high-performance, asynchronous website monitoring system built with **Python 3.13**. This tool checks the status of multiple URLs simultaneously and logs the results into a persistent **SQLite** database.

## 🚀 Features
* **Asynchronous I/O:** Uses `httpx` and `asyncio` to monitor dozens of sites in parallel without blocking.
* **Persistent Storage:** Every check is logged in a local SQLite database using `aiosqlite`.
* **Real-time Alerts:** Automatically detects and flags "DOWN" status for immediate visibility.
* **Automated Heartbeat:** Runs on a configurable loop (default: 60s) to provide continuous monitoring.

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/KilladiJoel/sentinel-automation.git](https://github.com/KilladiJoel/sentinel-automation.git)
   cd sentinel-automation
   ![Sentinel Output](screenshot.png)
